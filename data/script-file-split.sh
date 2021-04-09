#!/bin/bash
#Author: Jesimar da Silva Arantes
#Email: jesimar.arantes@gmail.com
#Date: 07/04/2021

echo "========== Script quebra arquivo em instancias menores =========="

#existem 167 instances na base de dados
for i in $(seq 167); do 			
	s=$((3*$i+1))
	head -n $s database.csv | tail -n 3 > instance-$i.csv
done

echo "====================== Operação Concluida ======================="
