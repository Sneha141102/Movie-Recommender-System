from flask import Flask,request,jsonify,render_template
import util
app = Flask(__name__,template_folder='template')
import numpy as np


@app.route('/')
def hello_world():
    return render_template('index.html')



@app.route('/get_movie_names')
def get_movie_names():
    response = util.get_movie_names()
    listToStr = ' , '.join([str(elem) for i,elem in enumerate(response)])
    #response.header.add('Acess-Control-Allow-Origin','*')
    return listToStr

@app.route('/recommend_movies',methods=['POST'])
def recommend_movie_names():
    print(str(request.form['s_movie']))
    movie = str(request.form['selected_movie'])
    recommendation = util.recommend(movie)
    r1 = recommendation[0]
    r2 = recommendation[1]
    r3 = recommendation[2]
    r4 = recommendation[3]
    r5 = recommendation[4]
    r6 = recommendation[5]

    posters = util.recommend_poster(movie)

    p1 = posters[0]
    p2 = posters[1]
    p3 = posters[2]
    p4 = posters[3]
    p5 = posters[4]
    p6 = posters[5]

    overview = util.recommend_overview(movie)

    o1 = overview[0]
    o2 = overview[1]
    o3 = overview[2]
    o4 = overview[3]
    o5 = overview[4]
    o6 = overview[5]
   
    return render_template('index.html',movie1="{}".format(r1),movie2="{}".format(r2),movie3="{}".format(r3),movie4="{}".format(r4),movie5="{}".format(r5),movie6="{}".format(r6),poster1="{}".format(p1),poster2="{}".format(p2),poster3="{}".format(p3),poster4="{}".format(p4),poster5="{}".format(p5),poster6="{}".format(p6),over1="{}".format(o1),over2="{}".format(o2),over3="{}".format(o3),over4="{}".format(o4),over5="{}".format(o5),over6="{}".format(o6))
    



if __name__=="__main__":
    app.run()

'''def recommend(movie):
    index = new[new['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        print(new.iloc[i[0]].title)

movies_list = pickle.load(open('movies.pkl','rb'))
movies_list = movies_list['title'].values'''