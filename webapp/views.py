
from django.shortcuts import render
from django.views.generic import TemplateView
import happybase
connection = happybase.Connection(host = 'localhost', port = 9090 , autoconnect = False)
connection.open()
tables = connection.tables()
import plotly.offline as opy
import plotly.graph_objs as go
from .forms import IndexForm, YearForm, MonthForm
# from .choices import *

# Create your views here.
class Index(TemplateView):
    template_name = 'webapp/index.html'
    # def index(request):
    #     context = {}
    #
    #     # return render(request, template_name)
    #     return render_to_response(template_name, context)

    def plot(self):
        table_year = connection.table('Years')
        data = {}
        Data = []
        flag = 0
        x = []
        y = []
        list_names = []
        for key, value in table_year.scan():
            # print(key, value)
            temp_string = str(key)
            temp_string = temp_string.strip("b")
            temp_string = temp_string.strip("\'")
            # print(temp_string)
            # data[temp_string] = [""]
            list_names.append(temp_string)
            if(flag == 0):
                flag = 1
                for k in value:
                    x.append(str(k).strip("b").strip("\'")[-4:])
            # print(value)
            temp_list = []
            for k in value:
                 temp_list.append(float(str((str(value[k]).strip("b")).strip("\'"))))
            data[temp_string] = temp_list

        # print("Data and x",data, x)

        for l in list_names:
            trace = go.Bar(
                x = x,
                y = data[l],
                name = l
            )
            Data.append(trace)

        layout = go.Layout(
            barmode = 'group'
        )

        fig = go.Figure(data = Data, layout = layout)
        div = opy.plot(fig, auto_open=False, output_type='div')

        # x = [-2, 0, 4, 6, 7]
        # y = [q**2-q+3 for q in x]
        # trace2 = go.Bar(x=x, y=y)
        # data = go.Data([trace2])
        # layout = go.Layout(title="Some Data Plotted !!! ", xaxis={'title': 'x1'}, yaxis={'title': 'x2'})
        # figure = go.Figure(data=data, layout=layout)
        # div = opy.plot(figure, auto_open=False, output_type='div')
        return div

    def get_context_data(self, **kwargs):
        the_form = IndexForm()
        context = super(Index, self).get_context_data(**kwargs)
        div = self.plot()
        context['index'] = div
        context['tables'] = tables
        context['form'] = the_form.as_p()
        context['title'] = 'IndexForm'
        return context



class Year(TemplateView):
    template_name = 'webapp/year.html'

    def plot(self, table_name):
        table_year = connection.table(table_name)
        data = {}
        Data = []
        flag = 0
        x = []
        y = []
        list_names = []
        for key, value in table_year.scan():
            # print(key, value)
            temp_string = str(key)
            temp_string = temp_string.strip("b")
            temp_string = temp_string.strip("\'")
            # print(temp_string)
            # data[temp_string] = [""]
            list_names.append(temp_string)
            if(flag == 0):
                flag = 1
                for k in value:
                    x.append(str(k).strip("b").strip("\'")[-4:])
            # print(value)
            temp_list = []
            for k in value:
                 temp_list.append(float(str((str(value[k]).strip("b")).strip("\'"))))
            data[temp_string] = temp_list

        # print("Data and x",data, x)

        for l in list_names:
            trace = go.Bar(
                x = x,
                y = data[l],
                name = l
            )
            Data.append(trace)

        layout = go.Layout(
            barmode = 'group'
        )

        fig = go.Figure(data = Data, layout = layout)
        div = opy.plot(fig, auto_open=False, output_type='div')

        # x = [-2, 0, 4, 6, 7]
        # y = [q**2-q+3 for q in x]
        # trace2 = go.Bar(x=x, y=y)
        # data = go.Data([trace2])
        # layout = go.Layout(title="Some Data Plotted !!! ", xaxis={'title': 'x1'}, yaxis={'title': 'x2'})
        # figure = go.Figure(data=data, layout=layout)
        # div = opy.plot(figure, auto_open=False, output_type='div')
        return div

    def get_context_data(self, **kwargs):

        context = super(Year, self).get_context_data(**kwargs)
        the_form = YearForm()
        context['form'] = the_form.as_p()
        context['title'] = 'YearForm'
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        # print(request.POST)
        # print(request.POST.get("url"))
        form = IndexForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            context['year'] = form.cleaned_data.get('year')
        context['index'] = self.plot('Y'+str(context['year']))
        return render(request, self.template_name, context)


class Month(TemplateView):
    template_name = 'webapp/month.html'

    def plot(self, table_name):
        table_year = connection.table(table_name)
        data = {}
        Data = []
        flag = 0
        x = []
        y = []
        list_names = []
        for key, value in table_year.scan():
            # print(key, value)
            temp_string = str(key)
            temp_string = temp_string.strip("b")
            temp_string = temp_string.strip("\'")
            # print(temp_string)
            # data[temp_string] = [""]
            list_names.append(temp_string)
            if(flag == 0):
                flag = 1
                for k in value:
                    x.append(str(k).strip("b").strip("\'")[-4:])
            # print(value)
            temp_list = []
            for k in value:
                 temp_list.append(float(str((str(value[k]).strip("b")).strip("\'"))))
            data[temp_string] = temp_list

        # print("Data and x",data, x)

        for l in list_names:
            trace = go.Bar(
                x = x,
                y = data[l],
                name = l
            )
            Data.append(trace)

        layout = go.Layout(
            barmode = 'group'
        )

        fig = go.Figure(data = Data, layout = layout)
        div = opy.plot(fig, auto_open=False, output_type='div')

        # x = [-2, 0, 4, 6, 7]
        # y = [q**2-q+3 for q in x]
        # trace2 = go.Bar(x=x, y=y)
        # data = go.Data([trace2])
        # layout = go.Layout(title="Some Data Plotted !!! ", xaxis={'title': 'x1'}, yaxis={'title': 'x2'})
        # figure = go.Figure(data=data, layout=layout)
        # div = opy.plot(figure, auto_open=False, output_type='div')
        return div

    def get_context_data(self, **kwargs):
        # the_form = SubmitUrlForm()
        context = super(Month, self).get_context_data(**kwargs)
        the_form = MonthForm()
        context['form'] = the_form.as_p()
        context['title'] = 'MonthForm'
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        # print(request.POST)
        # print(request.POST.get("url"))
        form = YearForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            context['year'] = request.POST.get('year')
            context['month'] = form.cleaned_data.get('month')
        context['index'] = self.plot('YM'+str(context['year'])+str(context['month']))
        return render(request, self.template_name, context)


class Date(TemplateView):
    template_name = 'webapp/date.html'

    def get_context_data(self, **kwargs):
        # the_form = SubmitUrlForm()
        context = super(Date, self).get_context_data(**kwargs)

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        # print(request.POST)
        # print(request.POST.get("url"))
        form = MonthForm(request.POST)
        if form.is_valid():
            print("form.cleaned_data = ",form.cleaned_data)
            print("request.POST = ",request.POST)
            context['year'] = request.POST.get('year')
            context['month'] = request.POST.get('month')
            context['day'] = form.cleaned_data.get('day')
        return render(request, self.template_name, context)

if __name__ == '__main__':
    main()
