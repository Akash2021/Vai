import warnings
warnings.filterwarnings("ignore")  
from playsound import playsound
import numpy as np
import torch
from num2words import num2words 
from hparams import HParams as hp
from audio import save_to_wav
from models import SSRN,Text2Mel
from lj_speech import vocab, idx2char, get_test_data

torch.set_grad_enabled(False)
text2mel = Text2Mel(vocab)
text2mel.load_state_dict(torch.load("ljspeech-text2mel.pth").state_dict())
text2mel = text2mel.eval()
ssrn = SSRN()
ssrn.load_state_dict(torch.load("ljspeech-ssrn.pth").state_dict())
ssrn = ssrn.eval()

#SENTENCES = [
#    "The birch canoe slid on the smooth planks.",
#    "Glue the sheet to the dark blue background.",
#    "It's easy to tell the depth of a well.",
#    "2 plus 2 is 4"
#]
#
#for i in range(len(SENTENCES)):
#    sentence = SENTENCES[i]
#    new_sentence=" " .join([num2words(w) if w.isdigit()  else w for w in sentence.split()])
#    normalized_sentence = "".join([c if c.lower() in vocab else '' for c in new_sentence])
#    print(normalized_sentence)
#    sentences = [normalized_sentence]
#    max_N = len(normalized_sentence)
#    L = torch.from_numpy(get_test_data(sentences, max_N))
#    zeros = torch.from_numpy(np.zeros((1, hp.n_mels, 1), np.float32))
#    Y = zeros
#    A = None
#
#    for t in range(hp.max_T):
#      _, Y_t, A = text2mel(L, Y, monotonic_attention=True)
#      Y = torch.cat((zeros, Y_t), -1)
#      _, attention = torch.max(A[0, :, -1], 0)
#      attention = attention.item()
#      if L[0, attention] == vocab.index('E'):  # EOS
#          break
#
#    _, Z = ssrn(Y)
#    
#    Z = Z.cpu().detach().numpy()
#    save_to_wav(Z[0, :, :].T, '%d.wav' % (i + 1))

def say(sentence):
    new_sentence=" " .join([num2words(w) if w.isdigit()  else w for w in sentence.split()])
    normalized_sentence = "".join([c if c.lower() in vocab else '' for c in new_sentence])
    print(normalized_sentence)
    sentences = [normalized_sentence]
    max_N = len(normalized_sentence)
    L = torch.from_numpy(get_test_data(sentences, max_N))
    zeros = torch.from_numpy(np.zeros((1, hp.n_mels, 1), np.float32))
    Y = zeros
    A = None

    for t in range(hp.max_T):
      _, Y_t, A = text2mel(L, Y, monotonic_attention=True)
      Y = torch.cat((zeros, Y_t), -1)
      _, attention = torch.max(A[0, :, -1], 0)
      attention = attention.item()
      if L[0, attention] == vocab.index('E'):  # EOS
          break

    _, Z = ssrn(Y)
    i=int(0)
    Z = Z.cpu().detach().numpy()
    save_to_wav(Z[0, :, :].T, '%d.wav' % (i + 1))
    playsound('1.wav')






  
