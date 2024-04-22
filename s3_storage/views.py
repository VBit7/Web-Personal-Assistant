from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.encoding import smart_str

from .models import S3File
from .forms import S3FileForm


def upload_file(request):
    if request.method == 'POST':
        form = S3FileForm(request.POST, request.FILES)
        if form.is_valid():
            s3_file = form.save(commit=False)
            s3_file.user = request.user
            s3_file.save()
            return redirect('file_list')
    else:
        form = S3FileForm()
    return render(request, 'upload_file.html', {'form': form})


def download_file(request, pk):
    s3_file = get_object_or_404(S3File, pk=pk)
    response = HttpResponse(s3_file.file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(s3_file.file)
    return response


def delete_file(request, pk):
    s3_file = get_object_or_404(S3File, pk=pk)
    s3_file.delete()
    return redirect('file_list')
