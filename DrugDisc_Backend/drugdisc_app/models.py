from django.db import models

# class Compound(models.Model):
#     # Represents a compound molecule
#     name = models.CharField(max_length=255)
#     # Define fields for atomic, physicochemical, and structural properties of the compound
#     atomic_weight = models.FloatField()
#     physicochemical_property = models.CharField(max_length=255)
#     structural_property = models.CharField(max_length=255)


# class Protein(models.Model):
#     # Represents a protein
#     name = models.CharField(max_length=255)
#     gene_name = models.CharField(max_length=255)
#     # Define fields for protein features
#     domain_structure = models.CharField(max_length=255)
#     binding_site = models.CharField(max_length=255)


# class Bioactivity(models.Model):
#     # Represents experimental bioactivity data
#     compound = models.ForeignKey(Compound, on_delete=models.CASCADE)
#     protein = models.ForeignKey(Protein, on_delete=models.CASCADE)
#     pChEMBL_value = models.FloatField()
#     # Define fields for other bioactivity-related data
#     # Example: assay_type = models.CharField(max_length=255)
#     # Example: interaction_type = models.CharField(max_length=255)
#     # Add more fields as needed

# class GeneratedMolecule(models.Model):
#     # compound = models.ForeignKey(Compound, on_delete=models.CASCADE)
#     compound_name = models.CharField(max_length=100)
#     # protein = models.ForeignKey(Protein, on_delete=models.CASCADE)
#     similarity_score = models.FloatField()
    

class InputData(models.Model):
    compound_name = models.CharField(max_length=100)
    smiles_notation = models.CharField(max_length=255)
    atomic_weight = models.FloatField()
    physicochemical_property = models.CharField(max_length=255)
    structural_property = models.CharField(max_length=255)
    # Add more fields as needed

    def __str__(self):
        return self.compound_name