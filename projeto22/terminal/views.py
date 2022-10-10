from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404 as error404
from django.http import HttpResponse
from .models import alunos,manha,almoco,janta
from . import urls

def viewindex(request):
	return render(request,'index.html')

# def viewtaluno(request):
# 	aluno=alunos.objects.all()
# 	return render(request,'taluno.html',{'ALUNOS':aluno})

def viewtservidor(request):
	return render(request,'tservidor.html')

def viewtcadaluno(request):
	return render(request,'tcadaluno.html')

def viewtpedir(request):
	return render(request,'tpedir.html')

def viewtalunos(request):
	aluno=alunos.objects.all()
	return render(request,'talunos.html',{'ALUNOS':aluno})

def viewtnvrefeicao(request):
	aluno=alunos.objects.all()
	return render(request,'tnvrefeicao.html',{'ALUNOS':aluno})

def viewtall(request):
	cafes=manha.objects.all()
	almocos=almoco.objects.all()
	jantas=janta.objects.all()
	return render(request,'tall.html',{'CAFE':cafes,'ALMOCO':almocos,'JANTA':jantas})

def viewtcafe(request):
	cafes=manha.objects.all()
	return render(request,'tcafe.html',{'CAFE':cafes})

def viewtalmoco(request):
	almocos=almoco.objects.all()
	return render(request,'talmoco.html',{'ALMOCO':almocos})

def viewtjanta(request):
	jantas=janta.objects.all()
	return render(request,'tjanta.html',{'JANTA':jantas})


def defbtncadaluno(request):
	if  request.method=="POST":

		nome=request.POST.get('nome')
		nomes=alunos.objects.filter(name=nome)
		
		email=request.POST.get('email')
		emails=alunos.objects.filter(email=email)

		if (not emails) and (not nomes):
			email=request.POST.get('email')
			nome=request.POST.get('nome')
			aluno=alunos(name=nome,email=email)
			aluno.save()
			aluno=alunos.objects.all()
			return render(request,'talunos.html',{'ALUNOS':aluno,'SucessAlert':"Aluno Salvo"})
		else:
			return render(request,'tcadaluno.html',{'ExistsAlert':"Pessoa já cadastrada"})
	else:
		return render(request,'tcadaluno.html',{'getError':"Acesso GET negado - 001"})


def defpedir(request):
	if  request.method=="POST":
		email=request.POST.get('email')
		nome=request.POST.get('nome')


def defbtndelaluno(request,id):
	try:
		aluno=error404(alunos,pk=id)
		aluno.delete()
		allaluno=alunos.objects.all()
		return render(request,'talunos.html',{'ALUNOS':allaluno,'DeletSucessesAlert':"Sucesso em desativar Aluno"})
	except:
		allaluno=alunos.objects.all()
		return render(request,'talunos.html',{'ALUNOS':allaluno,'DeletErrorAlert':"Erro em desativar Aluno"})


def defbtnpedir(request):
	if request.method=="POST":
		try:
			pessoa=request.POST.get('pessoa')
			pesqpessoa=error404(alunos,name=pessoa)

			opcao=request.POST.get('comida')

			if opcao == "Café":
				nome=request.POST.get('pessoa')
				pedidocafe=manha(aluno=nome,refeicao=opcao)
				pedidocafe.save()

				aluno=alunos.objects.all()
				return render(request,'tnvrefeicao.html',{'ALUNOS':aluno,'SucessAlert2':"Refeição Solicitada"})

			elif opcao == "Almoço":
				nome=request.POST.get('pessoa')
				pedidoalmoco=almoco(aluno=nome,refeicao=opcao)
				pedidoalmoco.save() 

				aluno=alunos.objects.all()
				return render(request,'tnvrefeicao.html',{'ALUNOS':aluno,'SucessAlert2':"Refeição Solicitada"})

			elif opcao == "Jantar":
				nome=request.POST.get('pessoa')
				pedidojanta=janta(aluno=nome,refeicao=opcao)
				pedidojanta.save() 

				aluno=alunos.objects.all()
				return render(request,'tnvrefeicao.html',{'ALUNOS':aluno,'SucessAlert2':"Refeição Solicitada"})

			elif opcao == "Comida":	
			
				aluno=alunos.objects.all()
				return render(request,'tnvrefeicao.html',{'ALUNOS':aluno,'FoodAlert':"Erro na solicitação"})
		except:
			aluno=alunos.objects.all()
			return render(request,'tnvrefeicao.html',{'ALUNOS':aluno,'NotExistsAlert':"Aluno Não encontrado"})
	
	else:
		return render(request,'tnvrefeicao.html',{'getError':"Acesso GET negado - 002"})

def defbtnencerrarcafe(request,id):
	cafe=error404(manha,pk=id)
	cafe.delete()
	return redirect('terminal:tcafe')

def defbtnencerraralmoco(request,id):
	almocos=error404(almoco,pk=id)
	almocos.delete()
	return redirect('terminal:talmoco')

def defbtnencerrarjanta(request,id):
	jantas=error404(janta,pk=id)
	jantas.delete()
	return redirect('terminal:tjanta')
