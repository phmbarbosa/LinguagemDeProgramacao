import platform

so = platform.system()
versao = platform.version()
arquitetura = platform.architecture()[0]

print("Informações do sistema:")
print(f"Sistema Operacional: {so}")
print(f"Versão: {versao}")
print(f"Arquitetura: {arquitetura}")
