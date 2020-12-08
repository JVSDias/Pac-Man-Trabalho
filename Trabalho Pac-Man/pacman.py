from agente import Agente
from labirinto import Labirinto
from turtle import *
from time import sleep
import time

start_time = time.time()

def main():
    # Simulação 1
    #um_agente_percorre_tudo()

    # Simulação 2
    #um_agente_vagueia()

    # Simulação 3
    #todos_vagueiam()

    # Simulação 4
    #agente_com_um_destino()

    # Simulação 5
    n_agentes_percorrem_tudo()

    done()

""" Simulações """

def um_agente_percorre_tudo():
    dimensao_da_matriz = 20
    lab = Labirinto(dimensao_da_matriz)
    id = 0
    agente = lab.add_pacman(id)

    intervalo_entre_frames = 0.1

    chegou_ao_fim = False
    while (not chegou_ao_fim):
        chegou_ao_fim = agente.percorrer()
        # Atualiza "frame"
        update()
        sleep(intervalo_entre_frames)


def n_agentes_percorrem_tudo():
    dimensao_da_matriz = 20
    lab = Labirinto(dimensao_da_matriz)
    id = 0
    n_agentes = 4
    intervalo_entre_frames = 0.1
    chegou_ao_fim = False
    agentes = lab.agentes

    for id in range(0, n_agentes):
        f = lab.add_pacman(id)
        
    while (not chegou_ao_fim):
        for id in agentes.keys():
            chegou_ao_fim = agentes[id].percorrer()
        update()
        sleep(intervalo_entre_frames)

def um_agente_vagueia():
    dimensao_da_matriz = 20
    lab = Labirinto(dimensao_da_matriz)
    id = 0
    pacman = lab.add_pacman(id)

    n_frames = 500
    intervalo_entre_frames = 0.1
    for _ in range(n_frames):
        pacman.vaguear()
        update()
        sleep(intervalo_entre_frames)

def todos_vagueiam():
    dimensao_da_matriz = 20
    lab = Labirinto(dimensao_da_matriz)
    id = 0
    pacman = lab.add_pacman(id)

    n_fantasmas = 10
    for id in range(1, n_fantasmas):
        f = lab.add_fantasma(id)

    n_frames = 500
    intervalo_entre_frames = 0.1

    agentes = lab.agentes
    for _ in range(n_frames):
        for id in agentes.keys():
            agentes[id].vaguear()
        # Atualiza "frame"
        update()
        sleep(intervalo_entre_frames)


def agente_com_um_destino():
    dimensao_da_matriz = 20
    lab = Labirinto(dimensao_da_matriz)
    id = 0
    agente = lab.add_pacman(id)

    origem = agente._posicao
    destino = lab.cel_aleatoria()

    lab.desenhar_celula(origem, 'red')
    lab.desenhar_celula(destino, 'green')

    intervalo_entre_frames = 0.1

    chegou_ao_destino = False
    while (not chegou_ao_destino):
        chegou_ao_destino = agente.ir_a(destino)
        # Atualiza "frame"
        update()
        sleep(intervalo_entre_frames)

main()
print("O programa demorou %s segundos para ser executado" % (time.time() - start_time))
