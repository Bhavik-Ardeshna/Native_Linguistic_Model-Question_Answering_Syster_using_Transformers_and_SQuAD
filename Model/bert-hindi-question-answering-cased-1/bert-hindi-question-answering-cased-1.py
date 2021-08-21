# -*- coding: utf-8 -*-
"""BERT_Fine_Tune.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vAG5VYWGNa_wE1SHeNFztTCf_GhPzxl2

# ***Fine Tunning the BERT multilingual model***

### cmd line to remove clonned repository
"""

!rm -rf /content/Native_Linguistic_Model-Question_Answering_Syster_using_Transformers_and_SQuAD

"""## Clonning GitHub Repo"""

!git clone https://github.com/Bhavik-Ardeshna/Native_Linguistic_Model-Question_Answering_Syster_using_Transformers_and_SQuAD.git

!cd /content/Native_Linguistic_Model-Question_Answering_Syster_using_Transformers_and_SQuAD

"""## Installing requirements.txt and other dependencies"""

!pip install -r /content/Native_Linguistic_Model-Question_Answering_Syster_using_Transformers_and_SQuAD/Question-Answering/requirements.txt

!pip install transformers

"""## Now Fine-Tune ***bert-base-multilingual-cased*** pre-trained model from Huggingface

### **Training** and **Validating** on a given datasets
"""

!python /content/Native_Linguistic_Model-Question_Answering_Syster_using_Transformers_and_SQuAD/Question-Answering/run_qa.py \
  --model_name_or_path bert-base-multilingual-cased \
  --train_file /content/Native_Linguistic_Model-Question_Answering_Syster_using_Transformers_and_SQuAD/Datasets/Main/hindi/hi_dataset.json \
  --validation_file /content/Native_Linguistic_Model-Question_Answering_Syster_using_Transformers_and_SQuAD/Datasets/Main/hindi/hi_val_dataset.json \
  --do_train \
  --do_eval \
  --per_device_train_batch_size 16 \
  --learning_rate 3e-5 \
  --num_train_epochs 2 \
  --max_seq_length 384 \
  --doc_stride 128 \
  --output_dir /content/Native_Linguistic_Model-Question_Answering_Syster_using_Transformers_and_SQuAD/Model/bert-hindi-question-answering-cased-1

"""### **Validating** on a given datasets """

!python /content/Native_Linguistic_Model-Question_Answering_Syster_using_Transformers_and_SQuAD/Question-Answering/run_qa.py \
  --model_name_or_path bert-base-multilingual-cased \
  --train_file /content/Native_Linguistic_Model-Question_Answering_Syster_using_Transformers_and_SQuAD/Datasets/Main/hindi/hi_dataset.json \
  --validation_file /content/Native_Linguistic_Model-Question_Answering_Syster_using_Transformers_and_SQuAD/Datasets/Main/hindi/hi_val_dataset.json \
  --do_eval \
  --per_device_train_batch_size 16 \
  --learning_rate 3e-5 \
  --num_train_epochs 2 \
  --max_seq_length 384 \
  --doc_stride 128 \
  --output_dir /content/Native_Linguistic_Model-Question_Answering_Syster_using_Transformers_and_SQuAD/Model/bert-hindi-question-answering-cased-1

"""### Load the Fine Tunned model and Tokenizers"""

from transformers import BertForQuestionAnswering, AutoTokenizer

modelname = '/content/SQuAD-Datasets-Hindi-English/hindi-bert-qa-model'

model = BertForQuestionAnswering.from_pretrained(modelname)
tokenizer = AutoTokenizer.from_pretrained(modelname)

"""### Create Pipeline for Predictions"""

from transformers import pipeline
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

"""### Testing on single data"""

context = 'सूर्य अथवा सूरज सौरमंडल के केन्द्र में स्थित एक तारा जिसके चारों तरफ पृथ्वी और सौरमंडल के अन्य अवयव घूमते हैं। सूर्य हमारे सौर मंडल का सबसे बड़ा पिंड है और उसका व्यास लगभग १३ लाख ९० हज़ार किलोमीटर है जो पृथ्वी से लगभग १०९ गुना अधिक है। [1] ऊर्जा का यह शक्तिशाली भंडार मुख्य रूप से हाइड्रोजन और हीलियम गैसों का एक विशाल गोला है। परमाणु विलय की प्रक्रिया द्वारा सूर्य अपने केंद्र में ऊर्जा पैदा करता है। सूर्य से निकली ऊर्जा का छोटा सा भाग ही पृथ्वी पर पहुँचता है जिसमें से १५ प्रतिशत अंतरिक्ष में परावर्तित हो जाता है, ३० प्रतिशत पानी को भाप बनाने में काम आता है और बहुत सी ऊर्जा पेड़-पौधे समुद्र सोख लेते हैं। [2] इसकी मजबूत गुरुत्वाकर्षण शक्ति विभिन्न कक्षाओं में घूमते हुए पृथ्वी और अन्य ग्रहों को इसकी तरफ खींच कर रखती है।  \nसूर्य से पृथ्वी की औसत दूरी लगभग १४,९६,००,००० किलोमीटर या ९,२९,६०,००० मील है तथा सूर्य से पृथ्वी पर प्रकाश को आने में ८.३ मिनट का समय लगता है। इसी प्रकाशीय ऊर्जा से प्रकाश-संश्लेषण नामक एक महत्वपूर्ण जैव-रासायनिक अभिक्रिया होती है जो पृथ्वी पर जीवन का आधार है। यह पृथ्वी के जलवायु और मौसम को प्रभावित करता है। सूर्य की सतह का निर्माण हाइड्रोजन, हिलियम, लोहा, निकेल, ऑक्सीजन, सिलिकन, सल्फर, मैग्निसियम, कार्बन, नियोन, कैल्सियम, क्रोमियम तत्वों से हुआ है। [3] इनमें से हाइड्रोजन सूर्य के सतह की मात्रा का ७४ % तथा हिलियम २४ % है। \nइस जलते हुए गैसीय पिंड को दूरदर्शी यंत्र से देखने पर इसकी सतह पर छोटे-बड़े धब्बे दिखलाई पड़ते हैं। इन्हें सौर कलंक कहा जाता है। ये कलंक अपने स्थान से सरकते हुए दिखाई पड़ते हैं। इससे वैज्ञानिकों ने निष्कर्ष निकाला है कि सूर्य पूरब से पश्चिम की ओर २७ दिनों में अपने अक्ष पर एक परिक्रमा करता है। जिस प्रकार पृथ्वी और अन्य ग्रह सूरज की परिक्रमा करते हैं उसी प्रकार सूरज भी आकाश गंगा के केन्द्र की परिक्रमा करता है। इसको परिक्रमा करनें में २२ से २५ करोड़ वर्ष लगते हैं, इसे एक निहारिका वर्ष भी कहते हैं। इसके परिक्रमा करने की गति २५१ किलोमीटर प्रति सेकेंड है। \n\n विशेषताएँ\n\nसूर्य एक  G-टाइप मुख्य अनुक्रम तारा है जो सौरमंडल के कुल द्रव्यमान का लगभग 99.86% समाविष्ट करता है। करीब नब्बे लाखवें भाग के अनुमानित चपटेपन के साथ, यह करीब-करीब गोलाकार है,[4] इसका मतलब है कि इसका ध्रुवीय व्यास इसके भूमध्यरेखीय व्यास से केवल 10 किमी से अलग है। [5] जैसा कि सूर्य  प्लाज्मा का बना हैं और ठोस नहीं है, यह अपने ध्रुवों पर की अपेक्षा अपनी भूमध्य रेखा पर ज्यादा तेजी से घूमता है। यह व्यवहार  अंतरीय घूर्णन के रूप में जाना जाता है और सूर्य के संवहन एवं कोर से बाहर की ओर अत्यधिक तापमान ढलान के कारण पदार्थ की आवाजाही की वजह से हुआ है। यह सूर्य के वामावर्त कोणीय संवेग के एक बड़े हिस्से का वहन करती है, जैसा क्रांतिवृत्त के उत्तरी ध्रुव से देखा गया और इस प्रकार कोणीय वेग पुनर्वितरित होता है। इस वास्तविक घूर्णन की अवधि भूमध्य रेखा पर लगभग 25.6 दिन और ध्रुवों में 33.5 दिन की होती है। हालांकि, सूर्य की परिक्रमा के साथ ही पृथ्वी के सापेक्ष हमारी लगातार बदलती स्थिति के कारण इस तारे का अपनी भूमध्य रेखा पर  स्पष्ट घूर्णन करीबन 28 दिनों का है। [6] इस धीमी गति के घूर्णन का केन्द्रापसारक प्रभाव सूर्य की भूमध्य रेखा पर के सतही गुरुत्वाकर्षण से 1.8 करोड़ गुना कमजोर है। ग्रहों के ज्वारीय प्रभाव भी कमजोर है और सूर्य के आकार को खास प्रभावित नहीं करते है। [7]\nसूर्य एक पॉपुलेशन I या भारी तत्व युक्त सितारा है। [8] सूर्य का यह गठन एक या एक से अधिक नजदीकी  सुपरनोवाओं से निकली धनुषाकार तरंगों द्वारा शुरू किया गया हो सकता है। [9] ऐसा तथाकथित पॉपुलेशन II (भारी तत्व-अभाव) सितारों में इन तत्वों की बहुतायत की अपेक्षा, सौरमंडल में भारी तत्वों की उच्च बहुतायत ने सुझाया है, जैसे कि सोना और यूरेनियम। ये तत्व, किसी सुपरनोवा के दौरान ऊष्माशोषी नाभकीय अभिक्रियाओं द्वारा अथवा किसी दूसरी-पीढ़ी के विराट तारे के भीतर न्यूट्रॉन अवशोषण के माध्यम से  रूपांतरण द्वारा, उत्पादित किए गए हो सकने की सर्वाधिक संभवना है। [8]\nसूर्य की चट्टानी ग्रहों के माफिक कोई निश्चित सीमा नहीं है। सूर्य के बाहरी हिस्सों में गैसों का घनत्व उसके केंद्र से बढ़ती दूरी के साथ तेजी से गिरता है। [10] बहरहाल, इसकी एक सुपारिभाषित आंतरिक संरचना है जो नीचे वर्णित है। सूर्य की त्रिज्या को इसके केंद्र से लेकर प्रभामंडल के किनारे तक मापा गया है। सूर्य का बाह्य प्रभामंडल दृश्यमान अंतिम परत है। इसके उपर की परते नग्न आंखों को दिखने लायक पर्याप्त प्रकाश उत्सर्जित करने के लिहाज से काफी ठंडी या काफी पतली है। [11] एक पूर्ण सूर्यग्रहण के दौरान, तथापि, जब प्रभामंडल को चंद्रमा द्वारा छिपा लिया गया, इसके चारों ओर सूर्य के  कोरोना का आसानी से देखना हो सकता है।  \nसूर्य का आंतरिक भाग प्रत्यक्ष प्रेक्षणीय नहीं है। सूर्य स्वयं ही विद्युत चुम्बकीय विकिरण के लिए अपारदर्शी है। हालांकि, जिस प्रकार भूकम्प विज्ञान पृथ्वी के आंतरिक गठन को प्रकट करने के लिए भूकंप से उत्पन्न तरंगों का उपयोग करता है, सौर भूकम्प विज्ञान En का नियम इस तारे की आंतरिक संरचना को मापने और दृष्टिगोचर बनाने के लिए दाब तरंगों ( पराध्वनी) का इस्तेमाल करता है। [12] इसकी गहरी परतों की खोजबीन के लिए  कंप्यूटर मॉडलिंग भी सैद्धांतिक औजार के रूप में प्रयुक्त हुए है।  \n कोर \n\n\nसूर्य का  कोर इसके केन्द्र से लेकर सौर त्रिज्या के लगभग 20-25% तक विस्तारित माना गया है। [13] इसका घनत्व 150 ग्राम/सेमी3 तक[14][15] (पानी के घनत्व का लगभग 150 गुना) और तापमान 15.7 करोड़ केल्विन के करीब का है। [15] इसके विपरीत, सूर्य की सतह का तापमान लगभग 5,800 केल्विन है। सोहो मिशन डेटा के हाल के विश्लेषण विकिरण क्षेत्र के बाकी हिस्सों की तुलना में कोर के तेज घूर्णन दर का पक्ष लेते है। [13] सूर्य के अधिकांश जीवन में, ऊर्जा p–p (प्रोटॉन-प्रोटॉन) श्रृंखलाEn कहलाने वाली एक चरणबद्ध श्रृंखला के माध्यम से नाभिकीय संलयन द्वारा उत्पादित हुई है; यह प्रक्रिया हाइड्रोजन को हीलियम में रुपांतरित करती है। [16] सूर्य की उत्पादित ऊर्जा का मात्र 0.8% CNO चक्र En से आता है। [17]\nसूर्य में कोर अकेला ऐसा क्षेत्र है जो संलयन के माध्यम से तापीय ऊर्जा की एक बड़ी राशि का उत्पादन करता है; 99% शक्ति सूर्य की त्रिज्या के 24% के भीतर उत्पन्न हुई है, तथा त्रिज्या के 30% द्वारा संलयन लगभग पूरी तरह से बंद कर दिया गया है। इस तारे का शेष  उस उर्जा द्वारा तप्त हुआ है जो कोर से लेकर संवहनी परतों के ठीक बाहर तक विकिरण द्वारा बाहर की ओर स्थानांतरित हुई है। कोर में संलयन द्वारा उत्पादित ऊर्जा को फिर उत्तरोत्तर कई परतों से होकर सौर प्रभामंडल तक यात्रा करनी होती है इसके पहले कि वह सूर्य प्रकाश अथवा कणों की गतिज ऊर्जा के रूप में अंतरिक्ष में पलायन करती है। [18][19]\nकोर में प्रोटॉन-प्रोटॉन श्रृंखला दरेक सेकंड 9.2×1037 बार पाई जाती है। यह अभिक्रिया चार मुक्त  प्रोटॉनों (हाइड्रोजन नाभिक) का प्रयोग करती है, यह हर सेकंड करीब 3.7×1038 प्रोटॉनों को  अल्फा कणों (हीलियम नाभिक) में तब्दील करती है (सूर्य के कुल ~8.9×1056 मुक्त प्रोटॉनों में से), या लगभग 6.2× 1011 किलो प्रति सेकंड। [19] हाइड्रोजन से हीलियम संलयन के बाद हीलियम ऊर्जा के रूप में संलयित द्रव्यमान का लगभग 0.7% छोड़ती है,[20] सूर्य 42.6 करोड़ मीट्रिक टन प्रति सेकंड की द्रव्यमान-ऊर्जा रूपांतरण दर पर ऊर्जा छोड़ता है, 384.6  योटा वाट (3.846 × 1026 वाट),[21] या 9.192× 1010 टीएनटी मेगाटनEn प्रति सेकंड। राशि ऊर्जा पैदा करने में नष्ट नहीं हुई है, बल्कि यह राशि बराबर की इतनी ही ऊर्जा में तब्दील हुई है तथा ढोकर उत्सर्जित होने के लिए दूर ले जाई गई, जैसा द्रव्यमान-ऊर्जा तुल्यता अवधारणा का वर्णन हुआ है। \nकोर में संलयन से शक्ति का उत्पादन सौर केंद्र से दूरी के साथ बदलता रहता है। सूर्य के केंद्र पर, सैद्धांतिक मॉडलों के आकलन में यह तकरीबन 276.5 वाट/मीटर3 होना है,[22]\n जीवन चक्र \n\nसूर्य आज सबसे अधिक स्थिर अवस्था में अपने जीवन के करीबन आधे रास्ते पर है। इसमें कई अरब वर्षों से नाटकीय रूप से कोई बदलाव नहीं हुआ है, \xa0और आगामी कई वर्षों तक यूँ ही अपरिवर्तित बना रहेगा। हालांकि, एक स्थिर हाइड्रोजन-दहन काल के पहले का और बाद का तारा बिलकुल अलग होता है। \n\n निर्माण \nसूर्य एक विशाल आणविक बादल के हिस्से के ढहने से करीब 4.57 अरब वर्ष पूर्व गठित हुआ है जो अधिकांशतः हाइड्रोजन और हीलियम का बना है और शायद इन्ही ने कई अन्य तारों को बनाया है। [23] यह आयु  तारकीय विकास के  कंप्यूटर मॉडलो के प्रयोग और न्यूक्लियोकोस्मोक्रोनोलोजीEn के माध्यम से आकलित हुई है। [24] परिणाम प्राचीनतम सौरमंडल सामग्री की रेडियोमीट्रिक तिथि के अनुरूप है, 4.567 अरब वर्ष। [25][26] प्राचीन  उल्कापातों के अध्ययन अल्पजीवी आइसोटोपो के स्थिर नाभिक के निशान दिखाते है, जैसे कि लौह-60, जो केवल विस्फोटित, अल्पजीवी तारों में निर्मित होता है। यह इंगित करता है कि वह स्थान जहां पर सूर्य बना के नजदीक एक या एक से ज्यादा सुपरनोवा अवश्य पाए जाने चाहिए। किसी नजदीकी सुपरनोवा से निकली आघात तरंग ने आणविक बादल के भीतर की गैसों को संपीडित कर सूर्य के निर्माण को शुरू किया होगा तथा कुछ क्षेत्र अपने स्वयं के गुरुत्वाकर्षण के अधीन ढहने से बने होंगे। [27] जैसे ही बादल का कोई टुकड़ा ढहा कोणीय गति के संरक्षण के कारण यह भी घुमना शुरू हुआ और बढ़ते दबाव के साथ गर्म होने लगा। बहुत बड़ी द्रव्य राशि केंद्र में केंद्रित हुई, जबकि शेष बाहर की ओर चपटकर एक डिस्क में तब्दील हुई जिनसे ग्रह व अन्य सौरमंडलीय निकाय बने। बादल के कोर के भीतर के गुरुत्व व दाब ने अत्यधिक उष्मा उत्पन्न की वैसे ही डिस्क के आसपास से और अधिक गैस जुड़ती गई, अंततः नाभिकीय संलयन को सक्रिय किया। इस प्रकार, सूर्य का जन्म हुआ। \n मुख्य अनुक्रम \n\nसूर्य अपनी मुख्य अनुक्रम अवस्था से होता हुआ करीब आधी राह पर है, जिसके दरम्यान नाभिकीय संलयन अभिक्रियाओ ने हाइड्रोजन को हीलियम में बदला। हर सेकंड, सूर्य की कोर के भीतर चालीस लाख टन से अधिक पदार्थ ऊर्जा में परिवर्तित हुआ है और न्यूट्रिनो व  सौर विकिरण का निर्माण किया है। इस दर पर, सूर्य अब तक करीब 100 पृथ्वी-द्रव्यमान जितना पदार्थ ऊर्जा में परिवर्तित कर चुका है। सूर्य एक मुख्य अनुक्रम तारे के रूप में लगभग 10 अरब साल जितना खर्च करेगा। [29]\n कोर हाइड्रोजन समापन के बाद \nसूर्य के पास एक सुपरनोवा के रूप में विस्फोट के लिए पर्याप्त द्रव्यमान नहीं है। बावजुद यह एक लाल दानव चरण में प्रवेश करेगा। सूर्य का तकरीबन 5.4 अरब साल में एक लाल दानव बनने का पूर्वानुमान है। [30] यह आकलन हुआ है कि सूर्य संभवतः पृथ्वी समेत सौरमंडल के आंतरिक ग्रहों की वर्तमान कक्षाओं को निगल जाने जितना बड़ा हो जाएगा। [31]\n\nइससे पहले कि यह एक लाल दानव बनता है, सूर्य की चमक लगभग दोगुनी हो जाएगी और पृथ्वी शुक्र जितना आज है उससे भी अधिक गर्म हो जाएगी। एक बार कोर हाइड्रोजन समाप्त हुई, सूर्य का उपदानव चरण में विस्तार होगा और करीब आधे अरब वर्षों उपरांत आकार में धीरे धीरे दोगुना जाएगा। उसके बाद यह, आज की तुलना में दो सौ गुना बड़ा तथा दसियों हजार गुना और अधिक चमकदार होने तक, आगामी करीब आधे अरब वर्षों से ज्यादा तक और अधिक तेजी से फैलेगा। यह लाल दानव शाखा का वह चरण है, जहां पर सूर्य करीब एक अरब वर्ष बिता चुका होगा और अपने द्रव्यमान का एक तिहाई के आसपास गंवा चुका होगा। [31]\nसूर्य के पास अब केवल कुछ लाख साल बचे है, पर वें बेहद प्रसंगपूर्ण है। प्रथम, कोर हीलियम चौंध में प्रचंडतापूर्वक सुलगता है और सूर्य चमक के 50 गुने के साथ, आज की तुलना में थोड़े कम तापमान के साथ, अपने हाल के आकार से 10 गुने के आसपास तक वापस सिकुड़ जाता है। \n सौर अंतरिक्ष मिशन \n\n\n\n\nसूर्य के निरीक्षण के लिए रचे गए प्रथम उपग्रह नासा के  पायनियर 5, 6, 7, 8 और 9 थे। यह 1959 और 1968 के बीच प्रक्षेपित हुए थे। इन यानों ने पृथ्वी और सूर्य से समान दूरी की कक्षा में सूर्य परिक्रमा करते हुए सौर वायु और सौर चुंबकीय क्षेत्र का पहला विस्तृत मापन किया। पायनियर 9 विशेष रूप से लंबे अरसे के लिए संचालित हुआ और मई 1983 तक डेटा संचारण करता रहा। [33][34]\n1970 के दशक में, दो अंतरिक्ष यान  हेलिओस और स्काईलैब अपोलो टेलीस्कोप माउंट En ने सौर वायु व सौर कोरोना के महत्वपूर्ण नए डेटा वैज्ञानिकों को प्रदान किए। हेलिओस 1 और 2 यान अमेरिकी-जर्मनी सहकार्य थे। इसने अंतरिक्ष यान को बुध की कक्षा के भीतर  की ओर ले जा रही कक्षा से सौर वायु का अध्ययन किया। [35] 1973 में स्कायलैब अंतरिक्ष स्टेशन नासा द्वारा प्रक्षेपित हुआ। इसने अपोलो टेलीस्कोप माउंट कहे जाने वाला एक सौर वेधशाला मॉड्यूल शामिल किया जो कि स्टेशन पर रहने वाले अंतरिक्ष यात्रियों द्वारा संचालित हुआ था। [36] स्काईलैब ने पहली बार सौर संक्रमण क्षेत्र का तथा सौर कोरोना से निकली पराबैंगनी उत्सर्जन का समाधित निरीक्षण किया। [36] खोजों ने कोरोनल मास एजेक्सन के प्रथम प्रेक्षण शामिल किए, जो फिर "कोरोनल ट्रांजीएंस्ट" और फिर कोरोनल होल्स कहलाये, अब घनिष्ठ रूप से सौर वायु के साथ जुड़े होने के लिए जाना जाता है। [35]\n1980 का सोलर मैक्सीमम मिशन नासा द्वारा शुरू किया गया था। यह अंतरिक्ष यान उच्च सौर गतिविधि और सौर चमक के समय के दरम्यान  गामा किरणों,  एक्स किरणों और सौर ज्वालाओं से निकली पराबैंगनी विकिरण के निरीक्षण के लिए रचा गया था। प्रक्षेपण के बस कुछ ही महीने बाद, हालांकि, किसी इलेक्ट्रॉनिक्स खराबी की वजह से यान जस की तस हालत में चलता रहा और उसने अगले तीन साल इसी निष्क्रिय अवस्था में बिताए। 1984 में स्पेस शटल चैलेंजर मिशन STS-41C ने उपग्रह को सुधार दिया और कक्षा में फिर से छोड़ने से पहले इसकी इलेक्ट्रॉनिक्स की मरम्मत की। जून 1989 में पृथ्वी के वायुमंडल में पुनः प्रवेश से पहले सोलर मैक्सीमम मिशन ने मरम्मत पश्चात सौर कोरोना की हजारों छवियों का अधिग्रहण किया। [37]\n1991 में प्रक्षेपित, जापान के योनकोह (सौर पुंज) उपग्रह ने एक्स-रे तरंग दैर्घ्य पर सौर ज्वालाओ का अवलोकन किया। मिशन डेटा ने वैज्ञानिकों को अनेकों भिन्न प्रकार की लपटों की पहचान करने की अनुमति दी, साथ ही दिखाया कि चरम गतिविधि वाले क्षेत्रों से दूर स्थित कोरोना और अधिक गतिशील व सक्रिय थी जैसा कि पूर्व में माना हुआ था। योनकोह ने एक पूरे सौर चक्र का प्रेक्षण किया लेकिन 2001 में जब एक कुंडलाकार सूर्यग्रहण हुआ यह आपातोपयोगी दशा में चला गया जिसकी वजह से इसका सूर्य के साथ जुडाव का नुकसान हो गया। यह 2005 में वायुमंडलीय पुनः प्रवेश दौरान नष्ट हुआ था। [38]\nआज दिन तक का सबसे महत्वपूर्ण सौर मिशन  सोलर एंड हेलिओस्फेरिक ओब्सर्वेटरी रहा है। 2 दिसंबर1995 को शुरू हुआ यह मिशन यूरोपीय अंतरिक्ष एजेंसी और नासा द्वारा संयुक्त रूप से बनाया गया था। [36] मूल रूप से यह दो-वर्षीय मिशन के लिए नियत हुआ था। मिशन की 2012 तक की विस्तारण मंजूरी अक्टूबर 2009 में हुई थी। [39] यह इतना उपयोगी साबित हुआ कि इसका अनुवर्ती मिशन  सोलर डायनमिक्स ओब्सर्वेटरी (एसडीओ) फरवरी, 2010 में शुरू किया गया था। [40] यह पृथ्वी और सूर्य के बीच  लाग्रंगियन बिंदु (जिस पर दोनों ओर का गुरुत्वीय खींचाव बराबर होता है) पर स्थापित हुआ। सोहो ने अपने प्रक्षेपण के बाद से अनेक तरंगदैर्ध्यों पर सूर्य की निरंतर छवि प्रदान की है। [36] प्रत्यक्ष सौर प्रेक्षण के अलावा, सोहो को बड़ी संख्या में धूमकेतुओं की खोज के लिए समर्थ किया गया है, इनमे से अधिकांश सूर्य के निवाले छोटे धूमकेतुEn है जो सूर्य के पास से गुजरते ही भस्म हो जाते है। [41]\n\nइन सभी उपग्रहों ने सूर्य का प्रेक्षण क्रांतिवृत्त के तल से किया है, इसलिए उसके भूमध्यरेखीय क्षेत्रों मात्र के विस्तार में प्रेक्षण किए गए है। यूलिसिस यान सूर्य के ध्रुवीय क्षेत्रों के अध्ययन के लिए 1990 में प्रक्षेपित हुआ था। इसने सर्वप्रथम बृहस्पति की यात्रा की, इससे पहले इसे क्रांतिवृत्त तल के ऊपर की दूर की किसी कक्षा में बृहस्पति के गुरुत्वीय बल के सहारे ले जाया गया था। संयोगवश, यह 1994 की बृहस्पति के साथ धूमकेतु शूमेकर-लेवी 9 की टक्कर के निरीक्षण के लिए अच्छी जगह स्थापित हुआ था। एक बार यूलिसिस अपनी निर्धारित कक्षा में स्थापित हो गया, इसने उच्च सौर अक्षांशों की सौर वायु और चुंबकीय क्षेत्र शक्ति का निरीक्षण करना शुरू कर दिया और पाया कि उच्च अक्षांशों पर करीब 750 किमी/सेकंड से आगे बढ़ रही सौर वायु उम्मीद की तुलना में धीमी थी, साथ ही पाया गया कि वहां उच्च अक्षांशों से आई हुई बड़ी चुंबकीय तरंगे थी जो कि बिखरी हुई  गांगेय कॉस्मिक किरणे थी। [42]\nवर्णमंडल की तात्विक बहुतायतता को  स्पेक्ट्रोस्कोपी अध्ययनों से अच्छी तरह जाना गया है, पर सूर्य के अंदरूनी ढांचे की समझ उतनी ही बुरी है। सौर वायु नमूना वापसी मिशन,  जेनेसिस, खगोलविदों द्वारा सीधे सौर सामग्री की संरचना को मापने के लिए रचा गया था। जेनेसिस 2004 में पृथ्वी पर लौटा, पर पृथ्वी के वायुमंडल में पुनः प्रवेश पर तैनात करते वक्त पैराशूट के विफल होने से यह अकस्मात् अवतरण से क्षतिग्रस्त हो गया था। गंभीर क्षति के बावजूद, कुछ उपयोगी नमूने अंतरिक्ष यान के नमूना वापसी मॉड्यूल से बरामद किए गए हैं और विश्लेषण के दौर से गुजर रहे हैं। [43]\nसोलर टेरेस्ट्रियल रिलेशंस ओब्सर्वेटरी (स्टीरियो) मिशन अक्टूबर 2006 में शुरू हुआ था। दो एक सामान अंतरिक्ष यान कक्षाओं में इस तरीके से प्रक्षेपित किए गए जो उनको (बारी बारी से) कहीं दूर आगे की ओर खींचते और धीरे धीरे पृथ्वी के पीछे गिराते। यह सूर्य और सौर घटना के  त्रिविम प्रतिचित्रण करने में समर्थ है, जैसे कि कोरोनल मास एजेक्सनEn। [44][45]\nभारतीय अंतरिक्ष अनुसंधान संगठन ने 2015-16 तक  आदित्य नामक एक 100 किलो के उपग्रह का प्रक्षेपण निर्धारित किया है। सोलर कोरोना की गतिशीलता के अध्ययन के लिए इसका मुख्य साधन एक कोरोनाग्राफEn होगा। [46]\n सन्दर्भ \n\n इन्हें भी देखें \n सूर्य देव\n\n\nश्रेणी:सौर मंडल\nश्रेणी:हिन्दी विकि डीवीडी परियोजना\n*\nश्रेणी:जी-प्रकार मुख्य अनुक्रम तारे'
nlp({
     "question":'पृथ्वी को सूर्य की परिक्रमा करने में कितने दिन लागते है?',
     "context":context
})

"""## **Utility Functions**

### Provide **"path of hindi-bert-qa-model.tar.gz"** and "path of model hindi-bert-qa-model"
"""

!tar -czvf "path of hindi-bert-qa-model.tar.gz" "path of model hindi-bert-qa-model"

"""### Download the tar.gz file """

path_of_tar_gz_model_file = ""

from google.colab import files
files.download(path_of_tar_gz_model_file)