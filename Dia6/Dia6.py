
with open('input_test.txt', 'r') as archivo:
    contenido = archivo.read()

    #!Primera parte Día6
    for index, character in enumerate(contenido):
        init_position = index
        current_sub_string = set()
        for sub_string in contenido[init_position:init_position+4]:
            current_sub_string.add(sub_string)
        if len(current_sub_string) == 4:
            print(current_sub_string)
            print(init_position + 4)
            break
    #!Segunda Parte día 6
    # for index, character in enumerate(contenido):
    #     init_position = index
    #     current_sub_string = set()
    #     for sub_string in contenido[init_position:init_position+14]:
    #         current_sub_string.add(sub_string)
    #     if len(current_sub_string) == 14:
    #         print(current_sub_string)
    #         print(init_position + 14)
    #         break
            

    
    