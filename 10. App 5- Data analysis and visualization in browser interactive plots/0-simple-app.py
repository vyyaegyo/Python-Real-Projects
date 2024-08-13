import justpy as jp

def app():
    # Create a Quasar page
    wp = jp.QuasarPage()
    # Add a header
    h1 = jp.QDiv(a=wp, text="Analysis of Course Review", classes="text-h2 text-center q-mt-lg")
    # Add a paragraph
    p1 = jp.QDiv(a=wp, text="These graphs represent Course Review Analysis", classes="text-body1 text-center q-mt-md")
    return wp
jp.justpy(app, port=8080)
