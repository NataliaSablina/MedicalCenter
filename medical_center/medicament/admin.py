from django.contrib import admin

from medicament.models import (
    CommentMedicament,
    MedicamentCategory,
    Medicament,
    MedicamentSellerRelations,
)

admin.site.register(MedicamentCategory)
admin.site.register(Medicament)
admin.site.register(MedicamentSellerRelations)
admin.site.register(CommentMedicament)
