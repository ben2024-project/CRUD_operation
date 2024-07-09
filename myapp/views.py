from django.shortcuts import render,redirect

from myapp.models import Category,Product

from myapp.forms import CategoryForm,ProductForm

from django.views.generic import View

class CategoryCreate(View):

    def get(self,request,*args,**kwargs):

        form_instance=CategoryForm()

        return render(request,"category_add.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=CategoryForm(request.POST)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("cat-add")
        
        else:

            return render(request,"category_add.html",{"form":form_instance})

class ProductCreate(View):

     def get(self,request,*args,**kwargs):

        form_instance=ProductForm()

        return render(request,"product_add.html",{"form":form_instance})
    
     def post(self,request,*args,**kwargs):

        form_instance=ProductForm(request.POST)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("product-add")
        
        else:

            return render(request,"product_add.html",{"form":form_instance})
        
class ProductList(View):

    def get(self,request,*args,**kwargs):

        qs=Product.objects.all()

        all_category=Category.objects.all()

        return render(request,"product_list.html",{"data":qs,"category":all_category})

class ProductDetail(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Product.objects.get(id=id)

        return render(request,"product_detail.html",{"data":qs})

class ProductDelete(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Product.objects.get(id=id).delete()

        return redirect("product-list")

class ProductUpdate(View):

     def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Product.objects.get(id=id)

        form_instance=ProductForm(instance=qs)

        return render(request,"product_edit.html",{"form":form_instance})
    
     def post(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")

        qs=Product.objects.get(id=id)


        form_instance=ProductForm(request.POST,instance=qs)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("product-list")
        
        else:

            return render(request,"product_edit.html",{"form":form_instance}) 

class CategoryFilter(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        category=Category.objects.get(id=id)

        qs=Product.objects.filter(category_name=category)

        all_category=Category.objects.all()

        return render(request,"category_filter.html",{"data":qs,"category":all_category})
    


