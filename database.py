import psycopg2
def getC():
	try:
		return psycopg2.connect(user='gerente_rh',password='123456',dat>
	except Exception as e:
		print(e)
		return None

