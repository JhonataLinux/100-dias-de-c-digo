from __future__ import annotations
from dataclasses import dataclass, asdict
from enum import Enum
from typing import Optional, List, Dict, Any, Tuple
from datetime import datetime
import json, os, heapq

class Prioridade(Enum):
    ALTA = 1
    MEDIA = 2
    BAIXA = 3

class Status(Enum):
    ABERTO = "ABERTO"
    ANDAMENTO = "ANDAMENTO"
    FECHADO = "FECHADO"

@dataclass
class Ticket:
    id: int
    cliente: str
    categoria: str
    prioridade: Prioridade
    descricao: str
    status: Status
    criado_em: str
    atualizado_em: str
    resolucao: Optional[str] = None

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Ticket":
        # TODO: reconverter strings em Enums
        return Ticket(
            id=d["id"],
            cliente=d["cliente"],
            categoria=d["categoria"],
            prioridade=Prioridade[d["prioridade"]],  # TODO conferir chave
            descricao=d["descricao"],
            status=Status[d["status"]],
            criado_em=d["criado_em"],
            atualizado_em=d["atualizado_em"],
            resolucao=d.get("resolucao"),
        )

    def to_dict(self) -> Dict[str, Any]:
        # TODO: converter Enums para .name antes de salvar
        data = asdict(self)
        data["prioridade"] = self.prioridade.name
        data["status"] = self.status.name
        return data

class HelpDesk:
    def __init__(self, caminho="tickets.json"):
        self.caminho = caminho
        self.tickets: List[Ticket] = []
        self._heap: List[Tuple[int, float, int]] = []  # (prioridade, ts, id)
        self.load()

    def _now(self) -> str:
        return datetime.now().isoformat(timespec="seconds")

    def _next_id(self) -> int:
        return (max((t.id for t in self.tickets), default=0) + 1)

    def _rebuild_heap(self) -> None:
        self._heap = []
        for t in self.tickets:
            if t.status != Status.FECHADO:
                ts = datetime.fromisoformat(t.criado_em).timestamp()
                heapq.heappush(self._heap, (t.prioridade.value, ts, t.id))

    def load(self) -> None:
        if os.path.exists(self.caminho):
            with open(self.caminho, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.tickets = [Ticket.from_dict(d) for d in data]
        else:
            self.tickets = []
        self._rebuild_heap()

    def save(self) -> None:
        with open(self.caminho, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self.tickets], f, ensure_ascii=False, indent=2)

    # === TODOs principais ===
    def criar_ticket(self, cliente: str, categoria: str, prioridade: Prioridade, descricao: str) -> Ticket:
        # TODO: criar, adicionar na lista, empurrar no heap, salvar e retornar
        t = Ticket(
            id=self._next_id(),
            cliente=cliente.strip(),
            categoria=categoria.strip(),
            prioridade=prioridade,
            descricao=descricao.strip(),
            status=Status.ABERTO,
            criado_em=self._now(),
            atualizado_em=self._now(),
        )
        self.tickets.append(t)
        ts = datetime.fromisoformat(t.criado_em).timestamp()
        heapq.heappush(self._heap, (t.prioridade.value, ts, t.id))
        self.save()
        return t

    def listar(self, status: Optional[Status]=None, prioridade: Optional[Prioridade]=None, cliente: Optional[str]=None) -> List[Ticket]:
        # TODO: aplicar filtros e ordenar por (status, prioridade, criado_em)
        lst = self.tickets
        if status:
            lst = [t for t in lst if t.status == status]
        if prioridade:
            lst = [t for t in lst if t.prioridade == prioridade]
        if cliente:
            lst = [t for t in lst if t.cliente.lower() == cliente.lower()]
        return sorted(lst, key=lambda t: (t.status.value, t.prioridade.value, t.criado_em))

    def atender_proximo(self) -> Optional[Ticket]:
        # TODO: tirar do heap, mudar para ANDAMENTO, salvar
        while self._heap:
            _, _, tid = heapq.heappop(self._heap)
            t = self._by_id(tid)
            if t and t.status != Status.FECHADO:
                t.status = Status.ANDAMENTO
                t.atualizado_em = self._now()
                self.save()
                return t
        return None

    def fechar_ticket(self, ticket_id: int, resolucao: str) -> Optional[Ticket]:
        # TODO: marcar como FECHADO, salvar
        t = self._by_id(ticket_id)
        if not t:
            return None
        t.status = Status.FECHADO
        t.resolucao = resolucao.strip()
        t.atualizado_em = self._now()
        self.save()
        return t

    def _by_id(self, ticket_id: int) -> Optional[Ticket]:
        for t in self.tickets:
            if t.id == ticket_id:
                return t
        return None


def menu():
    hd = HelpDesk()
    while True:
        print("\n1) Criar  2) Listar  3) Atender próximo  4) Fechar  5) Sair")
        op = input("Opção: ").strip()
        if op == "1":
            cliente = input("Cliente: ")
            categoria = input("Categoria (Instalação/Cobrança/Instabilidade...): ")
            pr = input("Prioridade (ALTA/MEDIA/BAIXA): ").upper()
            desc = input("Descrição: ")
            try:
                t = hd.criar_ticket(cliente, categoria, Prioridade[pr], desc)
                print(f"Ticket #{t.id} criado!")
            except KeyError:
                print("Prioridade inválida.")
        elif op == "2":
            for t in hd.listar():
                print(f"#{t.id} [{t.status.name}/{t.prioridade.name}] {t.cliente} - {t.categoria} :: {t.descricao}")
        elif op == "3":
            t = hd.atender_proximo()
            print(f"Próximo: #{t.id} ({t.prioridade.name}) - {t.cliente}") if t else print("Sem chamados na fila.")
        elif op == "4":
            tid = int(input("ID do ticket: "))
            res = input("Resolução: ")
            t = hd.fechar_ticket(tid, res)
            print(f"Fechado #{t.id}.") if t else print("ID não encontrado.")
        elif op == "5":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
