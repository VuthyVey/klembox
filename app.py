from flask import Flask, g, jsonify, json, render_template, send_file, redirect, url_for, request
import os
from html import unescape
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.Certificate("./klem-webapp-firebase-adminsdk-sl38z-e6ff073b87.json")
firebase_admin.initialize_app(cred, {
  'projectId': "klem-webapp",
})

db = firestore.client()

doc_ref = db.collection(u'users').document(u'alovelace')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})

subjects_ref = db.collection(u'subjects')
chapters_ref = db.collection(u'chapters')
lessons_ref = db.collection(u'lessons')
kits_ref = db.collection(u'kit')

app = Flask(__name__)

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def catch_all(path):
#     return render_template('serverdown.html')

# @app.route('/')
# def kitlanding():
#     return render_template('kitlanding.html')

@app.route('/')
def home():
    return render_template('about.html')


@app.route('/gallery/<kit>')
def video(kit):
    videoList = {}
    if (kit == "hydro"):
        videoList = {"title": "កសិកម្មប្រកបដោយនិរន្តភាព", "videos": [{"t": "របៀបបណ្តុះគ្រាប់បន្លែ", "link": "AeYiA9oS-Ic"},{"t": "ការបន្លាស់កូនបន្លែ", "link": "SI9iaAE1zKI"}]}
    elif (kit == "electro"):
        videoList =  videoList = {"title": "បញ្ចេញពន្លឺ", "videos": [
            {"t": "បន្ទុកអគ្គីសនី", "link": "4dFvlxWZzXg"},
            {"t": "ចរន្តអគ្គិសនី", "link": "oUhAgK4qNJI"},
            {"t": "ការតសៀគ្វីបែបសេរ៑ី", "link": "Zdf_dO0XNMU"},
            {"t": "តភ្ជាប់សៀគ្វីបែបខ្នែង", "link": "HKtYMIWQvY8"},
            {"t": "របៀបប្រើប្រាស់តារាងក្តារភ្លើង", "link": "G9pOl-YXcQc"},
            {"t": "របៀបប្រើរេស៊ីស្តង់", "link": "sR8yjzJHBnE"},
            {"t": "សៀគ្វីអគ្គិសនី", "link": "z-sCrMCyZNs"}
        ]}
    else:
        videoList = {"title": "កោសិកា និងមីក្រូទស្សន៍", "videos": [
            {"t": "ការណែនាំអំពីឧបករណ៍មីក្រូទស្សន៍", "link": "irn8YWVT9tg"},
            {"t": "ការផ្គុំឧបករណ៍មីក្រូទស្សន៍", "link": "kb-mojUi-KM"},
            {"t": "ការណែនាំអំពីសៀវភៅសិស្ស", "link": "CZggFZvNpBs"},
            {"t": "ការប្រមូលវត្ថុគំរូពិសោធន៍", "link": "_YyaXSK2BAc"},
            {"t": "បង្កើតផ្ទាំងស្លាយគំរូពិសោធន៍", "link": "TTJdTmA9xGw"},
            {"t": "ការមើល និងប្រើប្រាស់មីក្រូទស្សន៍", "link": "TgMqx1h6614"},
            {"t": "មើលមីក្រូទស្សន៍ជាមួយទូរស័ព្ទ", "link": "L7E1uTJ3Esk"},
            # {"t": "ការប្រើហ្វូលស្គូប", "link": "4lpKveglhWg"},
            # {"t": "មើលមីក្រូទស្សន៍ជាមួយទូរស័ព្ទ", "link": "L7E1uTJ3Esk"},
            {"t": "ធ្វើការពិសោធន៍កោសិកាខ្ទឹមបារាំង", "link": "8b0Yw7WQLyY"},
            {"t": "ការពិសោធន៍កោសិកាថ្ពាល់", "link": "MKnzaeWPawQ"},
            {"t": "ធ្វើការពិសោធន៍អេឡូដេ", "link": "IG__cq2idJE"},
            {"t": "ការពិសោធន៍អាមីដុង", "link": "PiPWsvEV4mU"}
        ]}
    
    

    return render_template('video-gallery.html', videos=videoList)


@app.route('/discover')
def discover():
    referrer = request.referrer
    print("referer is : " + referrer)
    return render_template('discover.html')

@app.route('/product')
def all_products():
    return render_template('store.html')

@app.route('/product/<kit>')
def product(kit):

    one_kit_ref = kits_ref.where(u'code', u'==', kit).get()
    product_content = {}
    for content in one_kit_ref: 
        print(u'{} => {}'.format(content.id, content.to_dict()))
        product_content = content.to_dict()
    # docs = chapters_ref.where(u'subject',u'==', sub_ref).stream()

    # chapter_list = []
    # # print(dir(docs))
    # for doc in docs:
    #     # print(f'{doc.id} => {doc.to_dict()}')
    #     chap_ref = doc.reference
    #     # print(chap_ref)
    #     lesson_list = []
    #     lessons = lessons_ref.where(u'chapter',u'==', chap_ref).stream()
    #     for lesson in lessons:
    #         # print(f'{lesson.id} => {lesson.to_dict()}')
    #         y = lesson.to_dict()
    #         y['id'] = lesson.id
    #         lesson_list.append(y)
    #     x = doc.to_dict()
    #     x["lessons"] = lesson_list
    #     chapter_list.append(x)
    #     # print(x)
        
    
    print(one_kit_ref)
    # content = {}
    
    # if (kit == "foldscope"):
    #     content = {"title": "Cell AND Microscope",
    #                 "kit": kit,
    #                 "subject": "biology",
    #                 "description": "This kit will allow the students to be able to explore the biology contents even deeper where students are able to use this kit to explore the microscopic world with their own sample.",
    #                 "benefit": ["allow students to conduct classrooms and home experiment to view the microscopic world" , "gain better understanding of the cell learning contents", "scientific method", "problem solving and creativity"],
    #                 "material": ["Glass slides x 4", 
    #                     "Cover slips x 4", 
    #                     "Pre-made glass slide (2pcs) x 1", 
    #                     "Tape x 1", 
    #                     "Scissors  x 1", 
    #                     "Eppendorf tubes x 2", 
    #                     "Tweezers  x 1", 
    #                     "Plastic pipettes   x 2", 
    #                     "Plastic Packaging x 10", 
    #                     "Student Guidebook x 1", 
    #                     "Safety Rule Poster x 1", 
    #                     "Packaging Sticker  x 1", 
    #                     "Label Sticker x 10", 
    #                     "Packaging Box x 1"
    #                     ],
    #                 "feature":["A portable and waterproof made from paper.", "Magnification of 140X and 2 micron resolution", "Make their own sample slide", "View bacteria blood cells and single-celled organisms insects fabrics organic tissues and more!"] }
    # elif (kit == "hydro"): 
    #     content = {"title": "ប្រអប់កសិកម្ម្រកបដោយនិរន្តភាព",
    #                 "kit": "hydro"}
    # elif (kit == "electro"):
    #     content = {"title": "ប្រអប់អគ្គិសនី",
    #                 "kit": "eletro"}
    # else:
    #     content = {}

    return render_template('product.html', content=product_content)

@app.route('/store')
def store():
    return render_template('store.html')

@app.route('/lesson')
def lesson_list():
    return render_template('lesson_list.html')


@app.route('/resource')
def about():
    return render_template('kitlanding.html')

# @app.route('/subject')
# def subject():
#     return render_template('subject.html')

# @app.route('/lesson')
# def lesson():
#     return render_template('lesson.html')



# @app.route('/7')
# def grade():
#     docs = subjects_ref.stream()
#     subject_list = []
#     for doc in docs:
#         print(f'{doc.id} => {doc.to_dict()}')
#         subject_list.append(doc.to_dict())

#     name = 'Vuthy'
#     data = [
#             {"khName": "Vuthsy", "link": "chapter/physic", "img": "https://uploads-ssl.webflow.com/5f731109d7cb3261e53fd2eb/5f732a9822b1cf4f984f3129_relativity.svg"}, 
#             {"khName": "Reaksmy", "link": "chapter/bio", "img": "https://uploads-ssl.webflow.com/5f731109d7cb3261e53fd2eb/5f736834b394812d528e5745_lab.svg"}
#         ]
#     print(subject_list)
#     return render_template('index.html', name=name, data=subject_list)

@app.route('/some-other-page')
def other_page():
    return render_template('other-page.html')


# @app.route('/homepage')
# def homeagain():
#     return render_template('homepage.html')

@app.route('/subject/<subject_name>/')
def subject_detail(subject_name):
    name = subject_name
    sub_ref = subjects_ref.where(u'name', u'==', name).get()[0].reference
    
    docs = chapters_ref.where(u'subject',u'==', sub_ref).stream()

    chapter_list = []
    # print(dir(docs))
    for doc in docs:
        # print(f'{doc.id} => {doc.to_dict()}')
        chap_ref = doc.reference
        # print(chap_ref)
        lesson_list = []
        lessons = lessons_ref.where(u'chapter',u'==', chap_ref).stream()
        for lesson in lessons:
            # print(f'{lesson.id} => {lesson.to_dict()}')
            y = lesson.to_dict()
            y['id'] = lesson.id
            lesson_list.append(y)
        x = doc.to_dict()
        x["lessons"] = lesson_list
        chapter_list.append(x)
        # print(x)
        
    
    print(chapter_list)

   
    return render_template('lesson_list.html', name=subject_name, data=chapter_list)

# # @app.route('/subject/<subject_name>/lesson/<lesson_id>')
# # def lesson(subject_name, lesson_id):

# #     lesson = lessons_ref.document(lesson_id).get().to_dict()
# #     # print(type(lesson['content']))
# #     # lesson['content'] = unescape(lesson['content'])
# #     return render_template('lesson_detail.html', lesson=lesson )



# @app.route('/download')
# def download():
#     # redirect(url_for('home'))
#     return  send_file("static/sample.pdf", as_attachment=True)

# @app.route('/new')
# def new():
#     # redirect(url_for('home'))
#     return render_template('new.html')
  

# @app.route('/offline.html')
# def offline():
#     return app.send_static_file('offline.html')


@app.route('/service-worker.js')
def sw():
    return app.send_static_file('service-worker.js'),200, {'Content-Type': 'text/javascript'}


if __name__ == '__main__':
    # app.run(debug=True, host="0.0.0.0", port=int(os.environ.get('PORT',8080)))
    app.run(debug=True)
