#!/bin/bash


while true;
do
	name=$(inotifywait -r -e close_write,create,delete,moved_to Content/ );
	python Update $name; 

done
