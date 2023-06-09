## CIFAR-100 dataseti yordamida 100 ta obyektni qaysi klassga tegishli ekanligini bashorat qilish

#### 1. ```CIFAR-100``` dataseti haqida qisqacha ma'lumot
```CIFAR-100``` dataseti - 100 ta turdagi 60 000 ta tasvirni o'z ichiga olgan ma'lumotlar to'plami hisoblanadi. Har bir tasvir 32x32 piksel o'lchamga va 3 ta qatlamli rang kanali(```RGB```)ga ega. ```CIFAR-100``` datasetidagi tasvirlar ikkiga bo'linadi: 50 000 ta o'qitish (```train data```) tasvir va 10 000 ta sinov (```test data```) tasvir. Har bir tasvir, 100 ta kategoriya bo'yicha taqsimlangan. 100 ta kategoriya, 20 ta yuqori darajali kategoriya(```superclass```) bo'yicha tuzilgan. Har bir yuqori darajali kategoriya, 5 ta kichik turdagi kategoriya(```fine class```)larni o'z ichiga oladi.

```CIFAR-100``` dataseti uchun 20 ta yuqori darajali kategoriyalar (```superclass```) va 100 ta kichik turdagi kategoriyalar (```fine class```) quyidagi jadvalda keltirib o'tilgan:

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
        
  * ```CNN yordamida model o'qitish.ipynb``` ni ishga tushiring. Usbu notebookda Keras.io saytidagi MNIST datasetini o'qib olish, uni train va test datalariga ajratish, datalarni size va shape larini train uchun moslash hamda normallashtirish ko'rsatilgan. Dataset yordamida Convolutional Neural Network ishlab chiqilgan va u yordamida model train va evaluate qilingan. Model h5 formatda saqlanadi. [Modelni yuklash](https://drive.google.com/file/d/1lCXcILjaUIy5IbIJtGpiWwIyv_6BHXJ7/view?usp=share_link)
  
![streamlit1](https://github.com/MisterFoziljon/CIFAR-100/blob/main/rasmlar/accuracy_and_loss.png)
  
  * Bundan tashqari ushbu notebook yordamida saqlangan modelni load qilish va yangi test qilish datalari yordamida bashorat qilish (predict) ko'rsatib o'tilgan.


#### 5. Proyektni streamlit yordamida deploy qilish.

        (sizning_env) C:\CIFAR-100> streamlit run CIFAR-100.py

  * Proyekt ```local server```da ishga tushadi va quyidagicha ko'rinishda bo'ladi:


![streamlit1](https://github.com/MisterFoziljon/CIFAR-100/blob/main/rasmlar/streamlit1.png)
  
  * Rasm faylini yuklab oling va ```Predict``` tugmachasini bosing. Model yuklab olingan tasvirni qaysi turkumga tegishli ekanligini bashorat qiladi. Bundan tashqari softmaxdan chiqqan ehtimollik natijasi ham ekranga chiqadi.


![streamlit2](https://github.com/MisterFoziljon/CIFAR-100/blob/main/rasmlar/streamlit2.png)
