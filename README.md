# Jump2Django

## 2023-05-13 ~


## models related
```
from models import Question, Answer

Question_sets = Question.object.all()
q = Question_sets[0]
print(q.subject)
q.subject = 'new subject'
q.save()
```