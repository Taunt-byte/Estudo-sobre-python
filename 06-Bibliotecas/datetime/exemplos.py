# ==========================================
# BIBLIOTECA DATETIME
# ==========================================

from datetime import date, datetime, time, timedelta

# ==========================================
# DATA ATUAL
# ==========================================

hoje = date.today()

print("Data atual:", hoje)
print("Dia:", hoje.day)
print("Mês:", hoje.month)
print("Ano:", hoje.year)


# ==========================================
# DATA E HORA ATUAIS
# ==========================================

agora = datetime.now()

print("\nData e hora:", agora)
print("Hora:", agora.hour)
print("Minuto:", agora.minute)
print("Segundo:", agora.second)


# ==========================================
# FORMATANDO DATAS
# ==========================================

data_formatada = agora.strftime("%d/%m/%Y")

print("\nData formatada:", data_formatada)

hora_formatada = agora.strftime("%H:%M:%S")

print("Hora formatada:", hora_formatada)

data_completa = agora.strftime("%A, %d de %B de %Y")

print("Data completa:", data_completa)


# ==========================================
# CONVERTENDO TEXTO EM DATA
# ==========================================

data_texto = "31/10/2026"

data_convertida = datetime.strptime(data_texto, "%d/%m/%Y")

print("\nData convertida:", data_convertida)


# ==========================================
# CRIANDO DATAS
# ==========================================

data = date(2026, 10, 31)

print("\nData criada:", data)


# ==========================================
# CRIANDO HORÁRIOS
# ==========================================

horario = time(14, 30, 0)

print("\nHorário:", horario)


# ==========================================
# OPERAÇÕES COM DATAS
# ==========================================

amanha = hoje + timedelta(days=1)

ontem = hoje - timedelta(days=1)

print("\nAmanhã:", amanha)
print("Ontem:", ontem)


# ==========================================
# DIFERENÇA ENTRE DATAS
# ==========================================

inicio = date(2026, 1, 1)
fim = date(2026, 12, 31)

diferenca = fim - inicio

print("\nDiferença em dias:", diferenca.days)


# ==========================================
# VERIFICANDO DIA DA SEMANA
# ==========================================

dias_semana = [
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado",
    "Domingo"
]

print("\nHoje é:", dias_semana[hoje.weekday()])


# ==========================================
# INTERVALOS DE TEMPO
# ==========================================

duracao = timedelta(hours=2, minutes=30)

print("\nDuração:", duracao)