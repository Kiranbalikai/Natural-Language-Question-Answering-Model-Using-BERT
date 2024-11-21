

from transformers import pipeline

question_answer = pipeline("question-answering")
context="""
K. K. Usha (3 July 1939 – 5 October 2020) was an Indian judge who served as
the chief justice of the Kerala High Court between 2000 and 2001. The first female judge on the court, she advocated for women's rights and for the elimination of all forms of discrimination. After retiring from the court, she served as the president of the Excise and Service Tax Appellate Tribunal and then headed an Indian People's Tribunal enquiry in 2005 and 2006 into communal violence in Orissa. The enquiry was disrupted by activists from the Sangh Parivar. In 2011, she served as a member of an IPT panel on human rights issues in Manipur.
 This portrait photograph of Usha in court dress was taken in May 2020."""

result= question_answer(question="what did usha do after court ?",context=context)
print(f"answer: ‘{result['answer']}'")


