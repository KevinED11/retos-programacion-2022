"""
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "R" (piedra), "P" (papel)
 *   o "S" (tijera).
 * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
"""

from typing import Union, Dict, Tuple, List


def match(lista: List[Tuple[str, str]]) -> str:
    scores: Dict[str, Union[str, Tuple[str, str, str]]] = {
        'Piedra': 'R',
        'Papel': 'P',
        'Tijera': 'S',
        'Resultado': ('Player1', 'Player2', 'Empate'),
    }

    points: Dict[str, int] = {
        'Player1': 0,
        'Player2': 0
    }

    if not isinstance(lista, List):
        return 'Tipo de entrada invalida'

    quieres_jugar: str = input('quieres jugar? presiona cualquier tecla para empezar o "exit" para salir: ').lower()

    while quieres_jugar != 'exit':
        for i, (mov1, mov2) in enumerate(lista):
            print(f'Jugada {i + 1}: {mov1} vs {mov2}')

            if mov1 not in scores.values() or mov2 not in scores.values():
                return 'Ingresa datos validos para jugar'
            if mov1 == mov2:
                points['Player1'] += 0
                points['Player2'] += 0
            elif mov1 == scores['Piedra'] and mov2 == scores['Tijera'] or mov1 == scores['Tijera'] and mov2 == scores[
                'Papel'] or mov1 == scores['Papel'] and mov2 == scores['Piedra']:
                points['Player1'] += 1
            elif mov2 == scores['Piedra'] and mov1 == scores['Tijera'] or mov2 == scores['Tijera'] and mov1 == scores[
                'Papel'] or mov2 == scores['Papel'] and mov1 == scores['Piedra']:
                points['Player2'] += 1

        return f"El jugador 1 ha ganado con {points['Player1']} puntos" if points['Player1'] > points[
            'Player2'] else f"el juego ha quedado en '{scores['Resultado'][2]}'" if points['Player1'] == points[
            'Player2'] else f"el jugador 2 ha ganado con {points['Player2']} puntos"


if __name__ == '__main__':
    print(match([("R", "S"), ("S", "R"), ("P", "S")]))
