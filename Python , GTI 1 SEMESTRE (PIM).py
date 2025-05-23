def escolher_opcao(opcoes, mensagem):
    print("\n" + mensagem)
    for i in range(len(opcoes)):
        print(str(i + 1) + ". " + opcoes[i])

    while True:
        escolha = input("Escolha uma opção (número): ")
        if escolha.isdigit():
            n = int(escolha)
            if n >= 1 and n <= len(opcoes):
                return n - 1
        print("Opção inválida. Tente novamente.")

def fazer_prova(perguntas):
    print("\nComeçando a prova...\n")
    acertos = 0
    total = len(perguntas)

    for i in range(total):
        pergunta = perguntas[i]
        print("Questão " + str(i + 1) + ": " + pergunta["question"])
        for j in range(len(pergunta["options"])):
            print("  " + str(j + 1) + ". " + pergunta["options"][j])

        while True:
            resposta = input("Sua resposta (número): ")
            if resposta.isdigit():
                n = int(resposta)
                if n >= 1 and n <= len(pergunta["options"]):
                    break
            print("Resposta inválida. Tente novamente.")

        # Ajusta índice da resposta para base 0
        if (n - 1) == pergunta["answer"]:
            print("Resposta correta!")
            acertos = acertos + 1
        else:
            # Exibindo a opção certa (1-based)
            print("Resposta errada. A resposta certa é: " + str(pergunta["answer"] + 1))

        print("Explicação: " + pergunta["explanation"] + "\n")

    print("Você acertou " + str(acertos) + " de " + str(total) + " questões.")

    porcentagem = (acertos * 100.0) / total

    if porcentagem >= 80.0:
        desempenho = "Excelente desempenho!"
    elif porcentagem >= 50.0:
        desempenho = "Bom desempenho, continue estudando."
    else:
        desempenho = "Precisa melhorar, estude mais e tente novamente."

    print("Seu desempenho: " + str(round(porcentagem, 1)) + "% - " + desempenho + "\n")

def main():
    quizzes = {
        "Tecnologia da Informação": {
            "iniciante": [
                {
                    "question": "O que é Hardware?",
                    "options": [
                        "Um sistema operacional",
                        "A parte física do computador",
                        "Um programa de planilha",
                        "Um navegador web",
                        "Um antivírus"
                    ],
                    "answer": 1,
                    "explanation": "Hardware refere-se à parte física do computador."
                },
                {
                    "question": "O que é Software?",
                    "options": [
                        "A parte física do computador",
                        "Um conjunto de instruções digitais",
                        "Um pendrive",
                        "Um mouse",
                        "Uma placa de vídeo"
                    ],
                    "answer": 1,
                    "explanation": "Software é um conjunto de instruções que dizem ao hardware o que fazer."
                },
                {
                    "question": "Qual destas opções é um navegador de internet?",
                    "options": [
                        "Paint",
                        "Google Chrome",
                        "WordPad",
                        "Excel",
                        "VLC Player"
                    ],
                    "answer": 1,
                    "explanation": "Google Chrome é um navegador de internet."
                },
                {
                    "question": "O que significa a sigla URL?",
                    "options": [
                        "Unidade Rápida de Leitura",
                        "Uniform Resource Locator",
                        "Usuário de Rede Local",
                        "Unidade de Registro Lógico",
                        "Universal Router Line"
                    ],
                    "answer": 1,
                    "explanation": "URL significa Uniform Resource Locator, que é o endereço de um recurso na web."
                },
                {
                    "question": "O que é um banco de dados?",
                    "options": [
                        "Um tipo de cabo de energia",
                        "Um sistema para armazenar e organizar informações",
                        "Uma memória RAM externa",
                        "Um editor de texto",
                        "Um tipo de navegador"
                    ],
                    "answer": 1,
                    "explanation": "Um banco de dados é um sistema para armazenar e organizar informações."
                },
                {
                    "question": "O que é backup?",
                    "options": [
                        "Um vírus",
                        "Cópia de segurança de dados",
                        "Impressão em nuvem",
                        "Hardware corrompido",
                        "Computador extra"
                    ],
                    "answer": 1,
                    "explanation": "Backup é uma cópia de segurança de dados para evitar perda."
                },
                {
                    "question": "Qual é o principal objetivo de um firewall?",
                    "options": [
                        "Proteger a rede contra acessos não autorizados",
                        "Melhorar o desempenho do PC",
                        "Gerenciar senhas",
                        "Fazer backup automático",
                        "Atualizar o sistema"
                    ],
                    "answer": 0,
                    "explanation": "Um firewall protege a rede contra acessos não autorizados."
                },
                {
                    "question": "Qual desses é um exemplo de sistema operacional?",
                    "options": [
                        "Windows",
                        "Excel",
                        "Google",
                        "USB",
                        "Android Studio"
                    ],
                    "answer": 0,
                    "explanation": "Windows é um exemplo de sistema operacional."
                },
                {
                    "question": "Qual tecnologia permite que dispositivos se conectem sem fio?",
                    "options": [
                        "USB",
                        "HDMI",
                        "Wi-Fi",
                        "Ethernet",
                        "VGA"
                    ],
                    "answer": 2,
                    "explanation": "Wi-Fi é a tecnologia que permite conexões sem fio."
                },
                {
                    "question": "O que é phishing?",
                    "options": [
                        "Uma técnica de criptografia",
                        "Um programa legítimo",
                        "Um golpe digital que rouba dados pessoais",
                        "Um tipo de antivírus",
                        "Um firewall avançado"
                    ],
                    "answer": 2,
                    "explanation": "Phishing é um golpe digital que visa roubar dados pessoais."
                },
                {
                    "question": "Qual das seguintes é uma linguagem de programação?",
                    "options": [
                        "Excel",
                        "Windows",
                        "Java",
                        "Google",
                        "Word"
                    ],
                    "answer": 2,
                    "explanation": "Java é uma linguagem de programação."
                },
                {
                    "question": "O que é um dispositivo de saída?",
                    "options": [
                        "Mouse",
                        "Monitor",
                        "Teclado",
                        "Scanner",
                        "Webcam"
                    ],
                    "answer": 1,
                    "explanation": "Um monitor é um dispositivo de saída que exibe informações."
                },
                {
                    "question": "Qual das opções abaixo é usada para edição de texto?",
                    "options": [
                        "Excel",
                        "Word",
                        "PowerPoint",
                        "Chrome",
                        "Windows Explorer"
                    ],
                    "answer": 1,
                    "explanation": "Word é um software usado para edição de texto."
                },
                {
                    "question": "O que é RAM?",
                    "options": [
                        "Memória de vídeo",
                        "Memória de acesso aleatório",
                        "Processador",
                        "Disco rígido",
                        "Roteador"
                    ],
                    "answer": 1,
                    "explanation": "RAM significa Memória de Acesso Aleatório, usada para armazenar dados temporariamente."
                },
                {
                    "question": "Qual é a função do botão “Salvar como”?",
                    "options": [
                        "Fechar o documento",
                        "Editar conteúdo",
                        "Salvar o arquivo com novo nome ou formato",
                        "Copiar para a nuvem",
                        "Apagar o documento"
                    ],
                    "answer": 2,
                    "explanation": "Salvar como permite salvar o arquivo com um novo nome ou formato."
                },
                {
                    "question": "Qual desses é um serviço de armazenamento na nuvem?",
                    "options": [
                        "Photoshop",
                        "Windows",
                        "Google Drive",
                        "Firefox",
                        "Excel"
                    ],
                    "answer": 2,
                    "explanation": "Google Drive é um serviço de armazenamento na nuvem."
                },
                {
                    "question": "Qual é a principal função de um sistema ERP?",
                    "options": [
                        "Navegar na internet",
                        "Editar vídeos",
                        "Gerenciar recursos empresariais",
                        "Criar imagens",
                        "Proteger o computador"
                    ],
                    "answer": 2,
                    "explanation": "Um sistema ERP é usado para gerenciar recursos empresariais."
                },
                {
                    "question": "O que é um domínio?",
                    "options": [
                        "Um nome usado para identificar um site",
                        "Um comando do Excel",
                        "Um plugin",
                        "Um banco de dados",
                        "Um teclado virtual"
                    ],
                    "answer": 0,
                    "explanation": "Um domínio é o nome que identifica um site na internet."
                },
                {
                    "question": "O que é login?",
                    "options": [
                        "Um software de áudio",
                        "Processo de autenticação de usuário",
                        "Um comando de rede",
                        "Um antivírus",
                        "Uma marca de computador"
                    ],
                    "answer": 1,
                    "explanation": "Login é o processo de autenticação de um usuário em um sistema."
                },
                {
                    "question": "Um sistema de “BI” é utilizado para:",
                    "options": [
                        "Criação de sites",
                        "Análise de dados e apoio à decisão",
                        "Desenvolver jogos",
                        "Criptografar dados",
                        "Executar antivírus"
                    ],
                    "answer": 1,
                    "explanation": "BI significa Business Intelligence, usado para análise de dados."
                }
            ]
        },
        "Python": {
            "iniciante": [
                {
                    "question": "Como iniciar um comentário em Python?",
                    "options": [
                        "<!--",
                        "#",
                        "//",
                        "/**",
                        "%%"
                    ],
                    "answer": 1,
                    "explanation": "Comentários em Python são iniciados com #."
                },
                {
                    "question": "Qual função imprime algo no terminal?",
                    "options": [
                        "echo()",
                        "print()",
                        "show()",
                        "write()",
                        "output()"
                    ],
                    "answer": 1,
                    "explanation": "A função print() é usada para imprimir no terminal."
                },
                {
                    "question": "Qual comando cria uma lista?",
                    "options": [
                        "x = {1,2,3}",
                        "x = (1,2,3)",
                        "x = [1,2,3]",
                        "x = <1,2,3>",
                        "x = list(1,2,3)"
                    ],
                    "answer": 2,
                    "explanation": "Listas em Python são criadas usando colchetes []."
                },
                {
                    "question": "O que será impresso? print(2 ** 3)",
                    "options": [
                        "6",
                        "5",
                        "8",
                        "9",
                        "4"
                    ],
                    "answer": 2,
                    "explanation": "2 ** 3 é 2 elevado a 3, que resulta em 8."
                },
                {
                    "question": "Qual desses é um tipo de dado booleano?",
                    "options": [
                        "\"True\"",
                        "True",
                        "\"yes\"",
                        "1",
                        "enable"
                    ],
                    "answer": 1,
                    "explanation": "True é um valor booleano em Python."
                },
                {
                    "question": "O que esse código retorna? x = \"Olá\" print(len(x))",
                    "options": [
                        "Erro",
                        "3",
                        "4",
                        "2",
                        "5"
                    ],
                    "answer": 2,
                    "explanation": "len(x) retorna o comprimento da string, que é 3."
                },
                {
                    "question": "Como se declara uma função em Python?",
                    "options": [
                        "function nome()",
                        "def nome():",
                        "func nome():",
                        "void nome()",
                        "declare nome()"
                    ],
                    "answer": 1,
                    "explanation": "Funções são declaradas com a palavra-chave def."
                },
                {
                    "question": "Qual função converte string para inteiro?",
                    "options": [
                        "string()",
                        "convert()",
                        "int()",
                        "input()",
                        "str()"
                    ],
                    "answer": 2,
                    "explanation": "A função int() converte uma string que representa um número em um inteiro."
                },
                {
                    "question": "Qual estrutura de controle é usada para repetição?",
                    "options": [
                        "if",
                        "while",
                        "def",
                        "break",
                        "return"
                    ],
                    "answer": 1,
                    "explanation": "while é uma estrutura de controle usada para repetição."
                },
                {
                    "question": "O que esse código imprime? for i in range(3): print(i)",
                    "options": [
                        "1 2 3",
                        "0 1 2 3",
                        "0 1 2",
                        "1 2",
                        "Erro"
                    ],
                    "answer": 2,
                    "explanation": "O loop imprime os números de 0 a 2."
                },
                {
                    "question": "Como definir uma string?",
                    "options": [
                        "\"texto\"",
                        "texto",
                        "str(texto)",
                        "print(texto)",
                        "input()"
                    ],
                    "answer": 0,
                    "explanation": "Strings são definidas entre aspas."
                },
                {
                    "question": "O que significa == em Python?",
                    "options": [
                        "Atribuição",
                        "Comparação de igualdade",
                        "Subtração",
                        "Concatenação",
                        "Multiplicação"
                    ],
                    "answer": 1,
                    "explanation": "== é o operador de comparação de igualdade."
                },
                {
                    "question": "Como se cria um dicionário?",
                    "options": [
                        "[]",
                        "()",
                        "{}",
                        "<>",
                        "="
                    ],
                    "answer": 2,
                    "explanation": "Dicionários são criados usando chaves {}."
                },
                {
                    "question": "Qual palavra-chave encerra um loop?",
                    "options": [
                        "stop",
                        "exit",
                        "break",
                        "return",
                        "close"
                    ],
                    "answer": 2,
                    "explanation": "break é usado para encerrar um loop."
                },
                {
                    "question": "Qual método adiciona item a uma lista?",
                    "options": [
                        "append()",
                        "add()",
                        "insert()",
                        "extend()",
                        "push()"
                    ],
                    "answer": 0,
                    "explanation": "append() adiciona um item ao final da lista."
                },
                {
                    "question": "Qual operador é usado para 'diferente de'?",
                    "options": [
                        "==",
                        "=!",
                        "!=",
                        "<>",
                        "=/="
                    ],
                    "answer": 2,
                    "explanation": "O operador != é usado para verificar se dois valores são diferentes."
                },
                {
                    "question": "O que faz o comando input()?",
                    "options": [
                        "Recebe dados do usuário",
                        "Mostra uma mensagem",
                        "Conecta à internet",
                        "Finaliza o programa",
                        "Cria uma lista"
                    ],
                    "answer": 0,
                    "explanation": "input() é usado para receber dados do usuário."
                },
                {
                    "question": "Qual é a saída? x = 10 x += 2 print(x)",
                    "options": [
                        "12",
                        "10",
                        "2",
                        "Erro"
                    ],
                    "answer": 0,
                    "explanation": "x += 2 adiciona 2 a x, resultando em 12."
                },
                {
                    "question": "O que é None?",
                    "options": [
                        "String",
                        "Número",
                        "Valor nulo",
                        "Lista",
                        "Boolean"
                    ],
                    "answer": 2,
                    "explanation": "None é um valor nulo em Python."
                },
                {
                    "question": "O que é indentação em Python?",
                    "options": [
                        "Uso de parênteses",
                        "Espaços que indicam blocos de código",
                        "Declaração de variáveis",
                        "Fechamento de funções",
                        "Tipagem de dados"
                    ],
                    "answer": 1,
                    "explanation": "Indentação é usada para definir blocos de código em Python."
                }
            ]
        },
        "Infraestrutura Computacional": {
            "iniciante": [
                {
                    "question": "O que é um servidor DNS?",
                    "options": [
                        "Converte nomes de domínio em IPs",
                        "Garante velocidade de rede",
                        "Armazena dados pessoais",
                        "Envia emails",
                        "Criptografa senhas"
                    ],
                    "answer": 0,
                    "explanation": "Um servidor DNS converte nomes de domínio em endereços IP."
                },
                {
                    "question": "O que é DHCP?",
                    "options": [
                        "Nome de um protocolo de segurança",
                        "Distribui IPs automaticamente",
                        "Um firewall avançado",
                        "Um modem",
                        "Um tipo de vírus"
                    ],
                    "answer": 1,
                    "explanation": "DHCP é um protocolo que distribui endereços IP automaticamente."
                },
                {
                    "question": "O que é roteador?",
                    "options": [
                        "Impressora de rede",
                        "Equipamento que distribui internet",
                        "Processador gráfico",
                        "Tipo de software",
                        "Firewall físico"
                    ],
                    "answer": 1,
                    "explanation": "Um roteador é um dispositivo que distribui a conexão de internet."
                },
                {
                    "question": "O que é IP dinâmico?",
                    "options": [
                        "Endereço IP que nunca muda",
                        "Protocolo de segurança",
                        "IP atribuído temporariamente",
                        "IP inválido",
                        "Nome de servidor"
                    ],
                    "answer": 2,
                    "explanation": "IP dinâmico é um endereço IP que é atribuído temporariamente."
                },
                {
                    "question": "O que significa uptime?",
                    "options": [
                        "Tempo que o sistema está funcionando sem falhas",
                        "Tempo de resposta",
                        "Tempo de inatividade",
                        "Tempo de execução de um programa",
                        "Tempo para reiniciar"
                    ],
                    "answer": 0,
                    "explanation": "Uptime é o tempo que o sistema está funcionando sem falhas."
                }
            ]
        }
    }

    while True:
        print("Bem-vindo ao sistema de quizzes!\n")
        
        topicos = []
        for k in quizzes:
            topicos.append(k)
        indice_topico = escolher_opcao(topicos, "Escolha o tópico do quiz:")
        topico_escolhido = topicos[indice_topico]

        niveis = []
        for k in quizzes[topico_escolhido]:
            niveis.append(k)
        indice_nivel = escolher_opcao(niveis, "Escolha o nível do quiz:")
        nivel_escolhido = niveis[indice_nivel]

        perguntas = quizzes[topico_escolhido][nivel_escolhido]

        fazer_prova(perguntas)

        opcao_final = escolher_opcao(
            ["Fazer outra prova", "Sair"],
            "O que deseja fazer agora?"
        )
        if opcao_final == 1:
            print("Obrigado por usar o sistema de quizzes. Até mais!")
            break

if __name__ == "__main__":
    main()

