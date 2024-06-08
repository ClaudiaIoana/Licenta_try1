# from transformers import AutoTokenizer
# import torch
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# 
# class TheModel:
#     def __init__(self):
#         self.tokenizer, self.model = self.load_falcon_model()
# 
#     def load_falcon_model(self):
#         tokenizer = AutoTokenizer.from_pretrained("C:\\LICENTA\\try3\\model\\model_and_tokenizer\\tokenizer")
#         model_path = "model\\model_and_tokenizer\\model_weights.pth"
#         print("Loading model...")
#         model = torch.load(model_path, map_location=torch.device('cpu'))
#         model.eval()
#         print("Model loaded successfully.")
#         return tokenizer, model
# 
# 
# model_instance = TheModel()
# 
# 
# 
# def predict_view(request):
#     if request.method == 'POST':
#         input_text = request.POST.get('input_text')
#         prediction = model_instance.predict(input_text)  # Reuse the model instance to make predictions
#         return JsonResponse({'prediction': prediction})
#     else:
#         return JsonResponse({'error': 'Only POST requests are allowed.'}, status=400)
