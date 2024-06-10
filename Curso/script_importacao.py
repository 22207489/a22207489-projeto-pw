from Curso.models import *
import json

Curso.objects.all().delete()

Disciplina.objects.all().delete()

Areas_Cientifica.objects.all().delete()

Projeto.objects.all().delete()

Linguagens_de_Programacoe.objects.all().delete()





with open('Curso/json/lig.json') as f:
    lig = json.load(f)

    for chave, info in lig.items():
        if chave == "courseDetail":
            curso_info = info  # Assigning the course details to a variable

            curso_criado = Curso.objects.create(
                nome_do_curso=curso_info.get("courseName"),
                codigo_curso=curso_info.get("courseCode"),
                apresentacao=curso_info.get("presentation"),
                objetivos=curso_info.get("objectives"),
                condicoes_de_acesso=curso_info.get("accessContidions"),
                oportunidades_de_carreira=curso_info.get("careerOportunities"),
                competencias=curso_info.get("competences"),
                creditos_do_curso=curso_info.get("courseECTS")
            )





areas_disciplinas = {
    "Investigação Operacional": "Matemáticas e Físicas",
    "Matemática I": "Matemáticas e Físicas",
    "Matemática II": "Matemáticas e Físicas",
    "Métricas Empresariais": "Matemáticas e Físicas",
    "Sistemas Operativos": "Arquiteturas e Sistemas Operativos",
    "Redes de Computadores": "Redes e Telecomunicações",
    "Algoritmia e Estruturas de Dados": "Programação e Engenharia de SW",
    "Engenharia de Software": "Programação e Engenharia de SW",
    "Fundamentos de Programação": "Programação e Engenharia de SW",
    "Linguagens de Programação I": "Programação e Engenharia de SW",
    "Linguagens de Programação II": "Programação e Engenharia de SW",
    "Programação Web": "Programação e Engenharia de SW",
    "Sistemas de Informação na Nuvem": "Programação e Engenharia de SW",
    "Sistemas Móveis Empresariais": "Programação e Engenharia de SW",
    "Bases de Dados": "Sistemas de Informação",
    "Engenharia de Requisitos e Testes": "Sistemas de Informação",
    "Fundamentos de Sistemas de Informação": "Sistemas de Informação",
    "Interação Humano-Máquina": "Interação Humano-Máquina",
    "Data Mining": "Dados e Inteligência Artificial",
    "Inteligência Artificial": "Dados e Inteligência Artificial",
    "Sistemas de Suporte à Decisão": "Dados e Inteligência Artificial",
    "Auditoria de Sistemas de Informação": "Gestão e Softskills",
    "Cálculo Financeiro": "Gestão e Softskills",
    "Competências Comportamentais": "Gestão e Softskills",
    "Contabilidade": "Gestão e Softskills",
    "Controlo de Gestão": "Gestão e Softskills",
    "Gestão Financeira": "Gestão e Softskills",
    "Instrumentos de Gestão": "Gestão e Softskills",
    "Motivação e Liderança": "Gestão e Softskills",
    "Teoria e Prática de Marketing": "Gestão e Softskills",
    "Trabalho Final de Curso": "Genérica",
}

# Dicionário para armazenar áreas científicas já criadas
areas_criadas = {}

with open('Curso/json/lig.json') as f:
    lig = json.load(f)
    for chave, info in lig.items():
        if chave == "courseFlatPlan":
            for disciplina_info in info:
                # Verifica se a área científica correspondente já foi criada
                nome_disciplina = disciplina_info["curricularUnitName"]
                if nome_disciplina in areas_disciplinas:
                    nome_area = areas_disciplinas[nome_disciplina]
                    if nome_area in areas_criadas:
                        # Se a área já existe, use a instância existente
                        area_cientifica = areas_criadas[nome_area]
                    else:
                        # Se a área não existe, crie-a e armazene no dicionário de áreas criadas
                        area_cientifica = Areas_Cientifica.objects.create(nome_area_cientifica=nome_area,curso=curso_criado)
                        areas_criadas[nome_area] = area_cientifica
                else:
                    # Se o nome da disciplina não estiver mapeado para uma área científica, defina a área como "Desconhecida"
                    area_cientifica = Areas_Cientifica.objects.create(nome_area_cientifica="Desconhecida")

                # Cria a instância da disciplina associada à área científica determinada
                Disciplina.objects.create(
                    nome_disciplina=nome_disciplina,
                    ano=disciplina_info["curricularYear"],
                    semestre=disciplina_info["semester"],
                    ects=disciplina_info["ects"],
                    curricularIUnitReadableCode=disciplina_info["curricularIUnitReadableCode"],
                    area_cientifica=area_cientifica,
                    horas_totais=disciplina_info["hrTotalContactoInt"]
                )


with open('Curso/json/lig_projetos.json') as f:
    projetos_data = json.load(f)

# Loop through the projects in the JSON
for projeto_data in projetos_data:
    # Get or create the associated Disciplina
    disciplina_nome = projeto_data["disciplina"]
    disciplina, _ = Disciplina.objects.get_or_create(nome_disciplina=disciplina_nome)

    # Create the project
    projeto = Projeto.objects.create(
        nome_do_projeto=projeto_data["nome"],
        descricao=projeto_data["descricao"],
        conceitos_aplicados=projeto_data["conceitos_aplicados"],
        imagem=projeto_data["imagem"],
        link_youtube=projeto_data["link_youtube"],
        link_github=projeto_data["link_github"],
        disciplina=disciplina
    )

    # Loop through the languages and add them to the project
    linguagens_utilizadas = projeto_data.get("tecnologias_utilizadas", [])
    for linguagem in linguagens_utilizadas:
        linguagem_obj, _ = Linguagens_de_Programacoe.objects.get_or_create(nome_de_linguagem=linguagem)
        projeto.tecnologias_utilizadas.add(linguagem_obj)

    projeto.save()

