from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def page(request):
    return render(request, 'main/page.html')


def page2(request):
    return render(request, 'main/page2.html')


def page3(request):
    return render(request, 'main/page3.html')

# header{
#     img {
#     position: relative;
#     top: 19px; left: 41px;
#     display: inline-block;
#     }
# }
# h1 {
# position: relative;
# top: 10px; left: 300px;
# color: black;
# font-size: 48px;
# font-family: Cormorant SC;
# font-weight: 400;
# word-wrap: break-word
#
#     }
# main {
# border-radius: 35px;
# background: #87C38F;
# width: 1800px;
# height: 790px;
# flex-shrink: 0;
#     div {
#         p{
#         color: #233D4C;
#         font-family: "Fira Sans Extra Condensed";
#         font-size: 36px;
#         font-style: normal;
#         font-weight: 400;
#         line-height: normal;
#         position: relative;
#         top: 235px; left: 144px;
#         width: 650px;
#         height: 193px;
#         flex-shrink: 0;
#         display: flex
#         }
#     }
#     p {
#     width: 761px;
#     height: 244px;
#     flex-shrink: 0;
#     color: #FFF;
#     font-family: "Fira Sans Extra Condensed";
#     font-size: 96px;
#     font-style: normal;
#     font-weight: 400;
#     line-height: normal;
#     position: relative;
#     top: 300px; left: 133px;
#     }
# }
