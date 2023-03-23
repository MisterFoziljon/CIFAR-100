## CIFAR-100 dataseti yordamida 100 ta obyektni qaysi klassga tegishli ekanligini bashorat qilish

#### 1. ```CIFAR-100``` dataseti haqida qisqacha ma'lumot
Yaqinda Zalando elektron tijorat kompaniyasi tadqiqotchilari ```Fashion MNIST```ni asl ```MNIST``` ma'lumotlar to'plamining o'rnini bosuvchi vosita sifatida taqdim etdilar. ```MNIST``` singari, ```Fashion MNIST``` ham 10 xil sinfga tegishli 60 000 ta o'quv tasvir(```train data```) va 10 000 ta sinov tasvir(```test data```)dan iborat to'plamidan iborat. Har bir o'quv misoli 28x28 o'lchamdagi kulrang kanalli rasmdir. Biz birinchi navbatda Fashion MNIST va MNIST o'rtasidagi farqlarni, shu jumladan har bir ma'lumot to'plamidagi modelning ishlashini ko'rib chiqamiz.

| Superclass             | Fine Classes                            |
|------------------------|----------------------------------------|
| Aquatic Mammals         | Beaver, Dolphin, Otter, Seal, Whale     |
| Fish                   | Aquarium Fish, Flatfish, Ray, Shark, Trout |
| Flowers                | Orchids, Poppies, Roses, Sunflowers, Tulips |
| Food Containers        | Bottles, Bowls, Cans, Cups, Plates      |
| Fruit and Vegetables   | Apples, Mushrooms, Oranges, Pears, Sweet Peppers |
| Household Electrical Devices | Clock, Computer Keyboard, Lamp, Telephone, Television |
| Household Furniture    | Bed, Chair, Couch, Table, Wardrobe       |
| Insects                | Bee, Beetle, Butterfly, Caterpillar, Cockroach |
| Large Carnivores       | Bear, Leopard, Lion, Tiger, Wolf         |
| Large Man-made Outdoor Things | Bridge, Castle, House, Road, Skyscraper |
| Large Natural Outdoor Scenes | Cloud, Forest, Mountain, Plain, Sea    |
| Large Omnivores and Herbivores | Camel, Cattle, Chimp, Elephant, Kangaroo |
| Medium-sized Mammals   | Fox, Porcupine, Possum, Raccoon, Skunk   |
| Non-insect Arthropods  | Crab, Lobster, Scorpion, Spider, Worm   |
| People                 | Baby, Boy, Girl, Man, Woman              |
| Reptiles               | Crocodile, Dinosaur, Lizard, Snake, Turtle |
| Small Mammals          | Hamster, Mouse, Rabbit, Shrew, Squirrel |
| Trees                  | Maple, Oak, Palm, Pine, Willow           |
| Vehicles 1             | Bicycle, Bus, Motorcycle, Pickup Truck, Train |
| Vehicles 2             | Lawn-mower, Rocket, Streetcar, Tank, Tractor |

![cmd](https://github.com/MisterFoziljon/CIFAR-100/blob/main/rasmlar/cifar100.png)

#### 2. Loyihani yuklab olish uchun quyidagi ketma-ketlikni bajaring:
  * `windows+R` klavishlarini bosing va paydo bo'lgan oynaga `cmd` buyrug'ini yozing OK tugmachasini bosing.
  
  ![cmd](https://github.com/MisterFoziljon/CIFAR-100/blob/main/rasmlar/cmd.png)

  * Loyihani quyidagi link yordamida yuklab oling. (Loyiha uchun yaratilgan fayl adresni o'zingiz ko'rsatishingiz mumkin)

        C:\> git clone https://github.com/MisterFoziljon/CIFAR-100.git

  * Loyiha joylashgan faylga kiring.
         
        C:\> cd CIFAR-100


#### 3. Proyektni ishlatish uchun kerakli modullarni virtual environment yaratib o'rnatib oling.
* O'zingizdagi pip ni so'nggi versiyasiga yangilang.

        C:\CIFAR-100> python -m pip install --upgrade pip
        
* virtual environment yaratish uchun virtualenv modulini o'rnating.
        
        C:\CIFAR-100> python -m pip install --user virtualenv

* Yangi environment yaratish uchun unga nom bering.
        
        C:\CIFAR-100> python -m venv sizning_env
        
* Virtual environmentni ishga tushiring(aktivlashtiring).
        
        C:\CIFAR-100> sizning_env\Scripts\activate.bat
        
* Virtual environment ichiga loyiha ishlashi uchun kerakli bo'lgan modullarni o'rnating (requirements.txt faylining ichida barchasi mavjud).
        
        (sizning_env) C:\CIFAR-100> pip install -r requirements.txt


#### 4. Proyektni ishlatish uchun jupyter notebook ni ishga tushiring.

        (sizning_env) C:\CIFAR-100> jupyter notebook
        
  * ```CNN yordamida model o'qitish.ipynb``` ni ishga tushiring. Usbu notebookda Keras.io saytidagi MNIST datasetini o'qib olish, uni train va test datalariga ajratish, datalarni size va shape larini train uchun moslash hamda normallashtirish ko'rsatilgan. Dataset yordamida Convolutional Neural Network ishlab chiqilgan va u yordamida model train va evaluate qilingan. Model h5 formatda saqlanadi. Ushbu notebookni birinchi bo'lib ishga tushirib ```modelni qayta o'qiting```!!! Chunki model githubga yuklanmadi.
  
![streamlit1](https://github.com/MisterFoziljon/CIFAR-100/blob/main/rasmlar/accuracy_and_loss.png)
  
  * ```Modelni sinovdan o'tkazish.ipynb``` ni ishga tushiring. Ushbu notebook yordamida saqlangan modelni load qilish va yangi test qilish datalari yordamida bashorat qilish (predict) ko'rsatib o'tilgan.


#### 4. Proyektni streamlit yordamida deploy qilish.

        (sizning_env) C:\CIFAR-100> streamlit run CIFAR-100.py

  * Proyekt ```local server```da ishga tushadi va quyidagicha ko'rinishda bo'ladi:


![streamlit1](https://github.com/MisterFoziljon/Fashion-MNIST/blob/main/rasmlar/streamlit1.png)
  
  * Rasm faylini yuklab oling va ```Predict``` tugmachasini bosing. Model yuklab olingan tasvirni qaysi turkumga tegishli ekanligini bashorat qiladi. Bundan tashqari softmaxdan chiqqan ehtimollik natijasi ham ekranga chiqadi.


![streamlit3](https://github.com/MisterFoziljon/CIFAR-100/blob/main/rasmlar/streamlit2.png)
