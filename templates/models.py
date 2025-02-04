from django.db import models

class Templates(models.Model):
    template_name = models.CharField(max_length=255)  
    structure = models.JSONField()                  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)      

    def __str__(self):
        return self.template_name  



class Content(models.Model):
    template = models.ForeignKey(Templates, on_delete=models.CASCADE)  
    content = models.JSONField() 
    section_type = models.CharField(max_length=50, default="general")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Contenido para {self.template.template_name}"
