from django.shortcuts import render
from django.http import HttpResponse
from AppRecetas.models import RecetasMain, RecetasUsr, Usuario 
from AppRecetas.forms import Form_AddRecetasMain, FormAddRecetasUsr , FormAddUsuario
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    return render(request,'AppRecetas/inicio.html')

# ingresar datos "C"UD 
def addRecetasMain(request):
  if request.method == "POST":#despues de dar click a eviar
    
    formulario1 = Form_AddRecetasMain(request.POST)
    
    if formulario1.is_valid():

      info =formulario1.cleaned_data

      res_Main = RecetasMain(nom_platos=info["nom_platos"],
                           ingredientes=request.POST["ingredientes"],
                           receta=request.POST["receta"],
                           tiempo=request.POST["tiempo"],
                           dificultad=request.POST["dificultad"],
                           tipoDeCocina=request.POST["tipoDeCocina"],
                           fuente=request.POST["fuente"], 
                           procedimiento=request.POST["procedimiento"])
      
      res_Main.save()                       
      return render(request,'AppRecetas/inicio.html')  
    
  else:
    formulario1 = Form_AddRecetasMain()

                         

  return render(request,'AppRecetas/addRecetasMain.html', {"form1" :formulario1})
  

def addRecetasUsr(request):
  
  if request.method == "POST":#despues de dar click a eviar
    
    formulario2 = FormAddRecetasUsr(request.POST)
    
    if formulario2.is_valid():

      info = formulario2.cleaned_data

      res_Usr = RecetasUsr(nom_platosUsr=info["nom_platosUsr"],
                           ingredientesUsr=info["ingredientesUsr"],
                           recetaUsr=info["recetaUsr"],
                           tiempoUsr=info["tiempoUsr"],
                           dificultadUsr=info["dificultadUsr"],
                           tipoDeCocinaUsr=info["tipoDeCocinaUsr"],
                           fuenteUsr=info["fuenteUsr"], 
                           procedimientoUsr=info["procedimientoUsr"])
      
      res_Usr.save()                       
      return render(request,'AppRecetas/inicio.html')  
    
  else:
    formulario2 = FormAddRecetasUsr()

                         

  return render(request,'AppRecetas/addRecetasUsr.html', {"form2" :formulario2})
                        

def addUsuario(request):
  if request.method == "POST":#despues de dar click a eviar
    
    formulario3 = FormAddUsuario(request.POST)
    
    if formulario3.is_valid():

      info = formulario3.cleaned_data

      addUsr = Usuario(nombreUsr=info["nombreUsr"],
                      emailUsr= info["emailUsr"],
                      telfonoUsr=info["telfonoUsr"],
                      ciudad=info["ciudad"],
                      edad =info["edad"],
      )
      addUsr.save()  
      
      return render(request,'AppRecetas/inicio.html')  
  else:
    formulario3 = FormAddUsuario()


  return render(request, "AppRecetas/addUsr.html", {"form3" : formulario3} )

#buscar y mostrar datos C"R"UD


def seekRecetas(request):

  return render(request, "AppRecetas/seekRecetas.html")

def showRecetas(request):

  if request.GET["ingredientes"]:

    ingreseek = request.GET["ingredientes"]
    recetasfind = RecetasMain.objects.filter(ingredientes__icontains=ingreseek)
    

    
    return render(request,"AppRecetas/showRecetas.html", {"ingreseek":ingreseek, "ingrefind": recetasfind ,  })

  else:
   respuesta ="No enviaste datos"  
   return HttpResponse(respuesta)                                 


def seekRecetasUsr(request):

  return render(request, "AppRecetas/seekRecetasUsr.html")


def showRecetasUsr(request):

  if request.GET["ingrediUsr"]:

    ingreseekUsr = request.GET["ingrediUsr"]
    recetasfindUsr = RecetasUsr.objects.filter(ingredientesUsr__icontains=ingreseekUsr)

    return render(request, "AppRecetas/showRecetasUsr.html", {"ingreBus" : ingreseekUsr, "recetasfoundUsr": recetasfindUsr})


  else:
   respuesta ="No enviaste datos"  
   return HttpResponse(respuesta)   



def seekUsr(request):
  return render(request,"AppRecetas/seekUsr.html")


def showUsr(request):

  if request.GET["Usr"]:

    ingreUsrseek = request.GET["Usr"]
    Usrfind = Usuario.objects.filter(nombreUsr__icontains=ingreUsrseek)
    

    
    return render(request,"AppRecetas/showUsr.html", {"ingreUsrseek":ingreUsrseek, "Usrfind": Usrfind })

  else:
   respuesta ="No enviaste datos"  
   return HttpResponse(respuesta)                                 



#modificar datos CR"U"D

def update_RecetasMain(request, recetas):
  
  recetas_eli = RecetasMain.objects.get(nom_platos=recetas)

  if request.method == "POST":#despues de dar click a eviar
    
    formulario1 = Form_AddRecetasMain(request.POST)
    
    if formulario1.is_valid():

      info = formulario1.cleaned_data

      recetas_eli.nom_platos = info["nom_platos"]
      recetas_eli.tipoDeCocina = info["tipoDeCocina"]
      recetas_eli.ingredientes = info["ingredientes"]
      recetas_eli.receta = info["receta"]
      recetas_eli.tiempo = info["tiempo"]
      recetas_eli.dificultad = info["dificultad"]
      recetas_eli.fuente = info["fuente"]
      recetas_eli.procedimiento = info["procedimiento"]
      
      recetas_eli.save() 
      
      return render(request,'AppRecetas/inicio.html')  

  else:

    formulario1 = Form_AddRecetasMain(initial ={  "nom_platos" : recetas_eli.nom_platos,
                                                  "tipoDeCocina" : recetas_eli.tipoDeCocina,
                                                  "ingredientes" : recetas_eli.ingredientes,
                                                  "receta" : recetas_eli.receta,
                                                  "tiempo" : recetas_eli.tiempo,
                                                  "dificultad" : recetas_eli.dificultad,
                                                  "fuente" :recetas_eli.fuente,
                                                  "procedimiento" : recetas_eli.procedimiento} )
  
  return render(request, "AppRecetas/updateRecetasMain.html", {"formulario1": formulario1 , "recetas" : recetas  } )    

    
def update_RecetasUsr(request, recetasUsr):

  recetas_eli_Usr = RecetasUsr.objects.get(nom_platosUsr=recetasUsr)

  if request.method == "POST":#despues de dar click a eviar
    
    formulario2 = Form_AddRecetasUsr(request.POST)
    
    if formulario2.is_valid():

      info = formulario2.cleaned_data

      recetas_eli_Usr.nom_platosUsr = info["nom_platosUsr"]
      recetas_eli_Usr.tipoDeCocinaUsr = info["tipoDeCocinaUsr"]
      recetas_eli_Usr.ingredientesUsr = info["ingredientesUsr"]
      recetas_eli_Usr.recetaUsr = info["recetaUsr"]
      recetas_eli_Usr.tiempoUsr = info["tiempoUsr"]
      recetas_eli_Usr.dificultadUsr = info["dificultadUsr"]
      recetas_eli_Usr.fuenteUsr = info["fuenteUsr"]
      recetas_eli_Usr.procedimientoUsr = info["procedimientoUsr"]
      
      recetas_eli_Usr.save() 
      
      return render(request,'AppRecetas/inicio.html')  

  else:

    formulario2 = FormAddRecetasUsr(initial ={  "nom_platosUsr" : recetas_eli_Usr.nom_platosUsr,
                                                  "tipoDeCocinaUsr" : recetas_eli_Usr.tipoDeCocinaUsr,
                                                  "ingredientesUsr" : recetas_eli_Usr.ingredientesUsr,
                                                  "recetaUsr" : recetas_eli_Usr.recetaUsr,
                                                  "tiempoUsr" : recetas_eli_Usr.tiempoUsr,
                                                  "dificultadUsr" : recetas_eli_Usr.dificultadUsr,
                                                  "fuenteUsr" :recetas_eli_Usr.fuenteUsr,
                                                  "procedimientoUsr" : recetas_eli_Usr.procedimientoUsr} )
  
  return render(request, "AppRecetas/updateRecetasUsr.html", {"formulario2": formulario2 , "recetasUsr" : recetasUsr  } )    




#def update_Usuario(request):
  
 #  pass

  




#para listar, recetas totales y usuarios ****listas***

def vista_recetasMain(request):

  recetasUsr_all = RecetasUsr.objects.all()
  recetasMain_all = RecetasMain.objects.all()

    
  return render(request,'AppRecetas/recetasMain.html', {"lista_recetasUsr" : recetasUsr_all , "lista_recetasMain": recetasMain_all})




def vista_recetasUsr(request):
  
  
  return render(request,'AppRecetas/recetasMain.html')



def vista_usuarios(request):
   usuario_all = Usuario.objects.all()
   listado = {"gente": usuario_all}

   return render(request, "AppRecetas/usuarios.html", listado )



#modificar datos CRU"D"    

def eliminarRecetasUsr(request, nom_recetasUsr):
  recetasUsr_eli = RecetasUsr.objects.get(nom_platosUsr=nom_recetasUsr)
  recetasUsr_eli.delete()

  recetasUsr_remain = RecetasUsr.objects.all()

  envioWeb ={"lista_recetasUsr": recetasUsr_remain}

  return render(request, "AppRecetas/recetasMain.html", envioWeb)


def eliminarRecetasMain(request, recetas):
  recetas_eli =RecetasMain.objects.get(nom_platos=recetas)
  recetas_eli.delete()

  
  recetas_remain = RecetasMain.objects.all()

  envWeb = {"lista_recetasMain": recetas_remain}

  return render(request, "AppRecetas/recetasMain.html", envWeb)






 






