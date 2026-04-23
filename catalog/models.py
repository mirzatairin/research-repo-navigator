from django.db import models

class ScientificTool(models.Model):
    name = models.CharField(max_length=200)
    developer = models.CharField(max_length=100)
    description = models.TextField(help_text="Describe the exoplanet model or tool.")
    repository_url = models.URLField(max_length=500, verbose_name="GitHub Link")
    
    # Categorization (similar to what EMAC uses)
    TOOL_TYPES = [
        ('SPEC', 'Spectroscopy'),
        ('ATM', 'Atmospheric Modeling'),
        ('SIM', 'Observation Simulation'),
        ('DA', 'Data Analysis'),
    ]
    category = models.CharField(max_length=4, choices=TOOL_TYPES, default='SIM')

    def __str__(self):
        return self.name