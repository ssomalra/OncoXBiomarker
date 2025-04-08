from django.shortcuts import render, get_object_or_404
from django.db.models import Prefetch
from django.db.models import Count
from .models import Cancer, Biomarker, BiomarkerImpact, Ref, BiomarkerImpactReference


def home(request):
    cancers = Cancer.objects.values('cancer_name').distinct()

    # Query for lung cancer subtypes and their biomarker counts
    lung_cancer_subtypes = (
        BiomarkerImpact.objects
        .filter(cancer__cancer_name__iexact='Lung')
        .values('cancer__subtype_name')
        .annotate(biomarker_count=Count('biomarker', distinct=True))
    )

    context = {
        'cancers': cancers,
        'lung_cancer_subtypes': lung_cancer_subtypes,
        'total_cancer_types': Cancer.objects.values('cancer_name').distinct().count(),
        'total_biomarkers': BiomarkerImpact.objects.values('biomarker').distinct().count(),
    }

    return render(request, 'home.html', context)

def help_page(request):
    cancers = Cancer.objects.values('cancer_name').distinct()  # Query cancer types
    context = {
        'cancers': cancers,  # Pass cancers to the template
    }
    return render(request, 'help.html', context)

def cancer_type_page(request, cancer_name):
    cancers = Cancer.objects.filter(cancer_name__iexact=cancer_name)
    if not cancers.exists():
        raise Http404("Cancer type not found.")
    all_cancers = Cancer.objects.values('cancer_name').distinct()

    impacts = BiomarkerImpact.objects.filter(cancer__in=cancers).select_related('biomarker', 'cancer').prefetch_related(
        Prefetch('biomarkerimpactreference_set', queryset=BiomarkerImpactReference.objects.select_related('reference'))
    )
    return render(request, 'cancer_type_page.html', {
        'cancer_name': cancer_name,
        'cancers': cancers,
        'all_cancers': all_cancers,
        'impacts': impacts
    })

def subtype_detail(request, subtype_name):
    cancer = get_object_or_404(Cancer, subtype_name__iexact=subtype_name)  # Fetch the cancer based on the subtype name
    cancers = Cancer.objects.values('cancer_name').distinct()  # Query cancer types
    context = {
        'cancer': cancer,  # Pass the specific cancer object
        'cancers': cancers,  # Pass all cancer types for the dropdown
    }
    return render(request, 'subtype_detail.html', context)

def biomarker_detail(request, biomarker_id):
    biomarker = get_object_or_404(Biomarker, pk=biomarker_id)
    cancers = Cancer.objects.values('cancer_name').distinct()  # Query cancer types
    context = {
        'cancers': cancers, 
        'biomarker': biomarker
    }
    return render(request, 'biomarker_detail.html', context)
