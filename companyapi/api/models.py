from django.db import models

# Company model
class Company(models.Model):
    
    company_id = models.AutoField(primary_key=True) # primary keys are read-only fields
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=
                            (('IT', 'Info Tech'),
                              ('NON IT', 'IT Infra'),
                              ('COMM', 'Telecom'))
                            )
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + ' at ' + self.location


# Employee model
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phno = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=100, choices=
                            (('Manager', 'Mgr'),
                              ('Software Developer', 'SD'),
                              ('Project Leader', 'PL'))
                            )
    # attribute / column to denote relationship
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
