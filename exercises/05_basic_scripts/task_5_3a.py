# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
mode_port = input ('Введите режим работы интерфейса (access/trunk): ')
port_number = input ('Ведите тип и номер интерфейса: ')
mode_vlan_choice = {
'access':'Введите номер VLAN',
'trunk':'Введите разрешенные VLANы'
}
vlan_number = input (mode_vlan_choice[mode_port])
interface = 'interface {}'
interface = interface.format(port_number)
choice_mode_port = {
'access': access_template,
'trunk': trunk_template
}
choice_mode_port = '\n'.join(choice_mode_port[mode_port]).format(vlan_number)
print('\n')
print(interface)
print(choice_mode_port)