usuarios =  ["pedro", "maria", "duda","dirceu", "elvis"]
senhas = ["123", "345", "567", "@@@$$$", "8910"]
usuario = input("Informe o nome de acesso ao sistema: ")
senha = int(input)"Informe a senha de acesso: "
for i in range (len(usuarios)):
    if usuarios[i] == usuario:
        resp = "Usuario Encontrado"
        break
    else:
        resp = "Usuario não encontrado"
print(resp)
