from django.shortcuts import render
from django.db.models import Q # Add this import for complex searching
from .models import ScientificTool

def tool_list(request):
    query = request.GET.get('q')
    if query:
        # Filter tools where name OR description contains the search text
        tools = ScientificTool.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        tools = ScientificTool.objects.all()
        
    return render(request, 'catalog/tool_list.html', {'tools': tools})


from django.shortcuts import redirect # Add this to your imports at the top
from .forms import ToolSubmissionForm

def submit_tool(request):
    if request.method == "POST":
        form = ToolSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tool_list') # Go back to the main list after saving
    else:
        form = ToolSubmissionForm()
    return render(request, 'catalog/submit_tool.html', {'form': form})