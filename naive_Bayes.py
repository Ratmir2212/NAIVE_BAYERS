inconsequential_words = ["the","all","off","of","or","but","and","through","though","although","then",
          "not","in","out","on","about","too","yet","nor","either","neither","so","therefore",
          "moreover","furthermore","however","also","hence","to","at","from","with","by","as",
          "this","that","these","those","between","only","for","a","an","into","non"," no","yes",
          "up","down","even","ever","am","is","are","was","were","will","i","he","she","we","they",
          "it","you","my","its","his","her","their","our","your","have","has","be","been","do","does",
          "not","thus","would","could","can","until","him","me","them","us","if","unless","who","when",
          "where","which","whether","what","why","whoever","whatever","whom","had","away","did","there",
          "whose","more","most","co","re","la","le","any","other","each","much","than","some","every",
          "thing","else","one","two","three","four","five","six","seven","eight","nine","ten"]

def cadef remove_inconsequent(text):
    new_text = ""
    all_words = set(text.split(" "))
    for word in all_words:
      if not word in inconsequential_words:
        new_text += word + " "
    return new_textlc_probs(d):
  """extend list words d from text
  return the dict of probabilities of words in this text"""
  dict_probs_d = {}
  d_set = set(d)
  for word in d_set:
    dict_probs_d[word] = d.count(word) / len(d)
  return dict_probs_d

path_spam_csv = "spam.csv"
import codecs
with codecs.open(path_spam_csv, "r",encoding='utf-8', errors='ignore') as fdata:
  segments = fdata.readlines()
  spam = []
  ham = []
  for i in segments:
      check = i.split(",")[0]
      if check == "spam":
          spam.append(i[5:].lower())  # spam
      else:
          ham.append(i[4:].lower())  # ham
  probs_spam = len(spam) / (len(spam) + len(ham))
  print(probs_spam)
  prob_spam = len(spam) / (len(ham) + len(spam))
  prob_ham = 1 - prob_spam
  print(prob_spam)
  print(prob_ham)
  all_spam_segments = []
  clear_spam = []
  for segment in spam:
      clear_spam.append(remove_inconsequent(segment))

  clear_ham = []
  for segment in ham:
      clear_ham.append(remove_inconsequent(segment))
  for segment in clear_spam:
      all_spam_segments += segment.split(" ")

  all_ham_segments = []
  for segment in clear_ham:
      all_ham_segments += segment.split(" ")

  P_words_spam = calc_probs(all_spam_segments)
  P_words_ham = calc_probs(all_ham_segments)
  from math import log


  def prediction(text):
      probs_spam = [P_words_spam[word] for word in text.split(" ") if word in P_words_spam]
      spam_value = abs(log(prob_spam)) + sum([abs(log(x)) for x in probs_spam])

      probs_ham = [P_words_ham[word] for word in text.split(" ") if word in P_words_ham]
      ham_value = abs(log(prob_ham)) + sum([abs(log(x)) for x in probs_ham])

      if spam_value > ham_value:
          return "spam"
      else:
          return "ham"