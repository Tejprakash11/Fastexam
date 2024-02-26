# from flask import Flask, render_template, request, redirect, url_for
# import PyPDF2

# app = Flask(__name__)

# def extract_text_from_pdf(file):
#     pdf_reader = PyPDF2.PdfFileReader(file)
#     text = ''
#     for page_num in range(pdf_reader.numPages):
#         text += pdf_reader.getPage(page_num).extractText()
#     return text

# @app.route('/', methods=['GET', 'POST'])
# def upload_question_paper():
#     if request.method == 'POST':
#         # Handle file upload
#         question_file = request.files['question_file']
        
#         # Process uploaded question paper file
#         question_text = extract_text_from_pdf(question_file)
        
#         # Store the question paper text in session for use in exam form
#         session['question_text'] = question_text
        
#         # Redirect to exam form page
#         return redirect(url_for('exam_form'))
    
#     return render_template('upload_form.html')

# @app.route('/exam-form', methods=['GET', 'POST'])
# def exam_form():
#     if request.method == 'POST':
#         # Process exam form submission
#         # You can access submitted answers using request.form
        
#         # For demonstration, let's assume we have a list of questions and answers
#         # and we check the submitted answers against the correct answers
#         questions = session.get('question_text').split('\n')  # Retrieve questions from session
#         correct_answers = ['b', 'a']  # Assume correct answers for demonstration purposes
        
#         submitted_answers = [request.form.get(f'question{i+1}') for i in range(len(questions))]
        
#         # Calculate score
#         score = sum(1 for sub_ans, correct_ans in zip(submitted_answers, correct_answers) if sub_ans == correct_ans)
        
#         # Render exam result page
#         return render_template('exam_result.html', score=score)
    
#     # Render exam form page with questions from session
#     return render_template('exam_form.html', questions=session.get('question_text').split('\n'))

# if __name__ == '__main__':
#     app.secret_key = 'your_secret_key_here'  # Needed for session
#     app.run(debug=True)





from flask import Flask, render_template, request, redirect, url_for, session
import PyPDF2

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for session

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ''
    for page_num in range(pdf_reader.numPages):
        text += pdf_reader.getPage(page_num).extractText()
    return text

@app.route('/', methods=['GET', 'POST'])
def upload_question_paper():
    if request.method == 'POST':
        # Handle file upload
        question_file = request.files['question_file']
        
        # Process uploaded question paper file
        question_text = extract_text_from_pdf(question_file)
        
        # Store the question paper text in session for use in exam form
        session['question_text'] = question_text
        
        # Redirect to exam form page
        return redirect(url_for('exam_form'))
    
    return render_template('../templates/upload_form.html')

@app.route('/exam-form', methods=['GET', 'POST'])
def exam_form():
    if request.method == 'POST':
       
        questions = session.get('question_text').split('\n')  # Retrieve questions from session
        correct_answers = ['b', 'a']  # Assume correct answers for demonstration purposes
        
        submitted_answers = [request.form.get(f'question{i+1}') for i in range(len(questions))]
        
        # Calculate score
        score = sum(1 for sub_ans, correct_ans in zip(submitted_answers, correct_answers) if sub_ans == correct_ans)
        
        # Render exam result page
        return render_template('exam_result.html', score=score)
    
    # Render exam form page with questions from session
    return render_template('../templates/exam_form.html', questions=session.get('question_text').split('\n'))

if __name__ == '__main__':
    app.run(debug=True)
