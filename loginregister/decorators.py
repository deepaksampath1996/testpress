from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('start')
        else:    
            return view_func(request,*args,**kwargs)
    return wrapper_func    


# def no_return(view_func):
#     def wrapper_func(request,*args,**kwargs):
#         if request.user.is_authenticated:
#             return redirect('result')
#         else:    
#             return view_func(request,*args,**kwargs)
#     return wrapper_func        

# # def no_no_return(view_func):
# #     def wrapper_func(request,*args,**kwargs):
# #         if request.user.is_authenticated:
# #             return redirect('result')
# #         else:    
# #             return view_func(request,*args,**kwargs)
# #     return wrapper_func            