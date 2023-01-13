# Этот репозиторий создан для автотестов написанных на языке Python и инструмента Selenium WebDriver в среде PyCharm.
Программный модуль «Система интерактивных электронных технических руководств» (ПМ ИЭТР) предназначен для информационной поддержки процессов технического обслуживания и ремонта изделия в эксплуатации, обеспечивающих эффективное использование изделия на всём протяжении его жизненного цикла. С помощью ПМ ИЭТР осуществляется просмотр электронной эксплуатационной и ремонтной документации с использованием веб-браузера.

ПМ ИЭТР обеспечивает просмотр структуры эксплуатационной и ремонтной документации (ЭРД), фильтрацию структуры документации с учётом вариантов использования изделия, выбор в структуре ЭРД модулей данных для просмотра, поиск данных по публикациям и модулям данных. Использование ПМ ИЭТР позволяет предоставить в интерактивном режиме справочную и описательную информацию об эксплуатационных и ремонтных процедурах, относящихся к конкретному изделию, а также перечень неисправностей и алгоритмы с объёмами работ по их устранению. Исходными данными для работы в ПМ ИЭТР являются публикации ЭРД, подготовленные в виде ИЭТР средствами автоматизированной разработки эксплуатационной и ремонтной документации в формате XML (eXtensible Markup Language – расширяемый язык разметки). Публикации ЭРД в виде ИЭТР должны быть подготовлены в соответствии с требованиями ГОСТ Р 54088-2017 и спецификации ASD S1000D.

<h1 align="center">Пример представления информации в ПМ ИЭТР приведён на рисунке 1:

![image](https://user-images.githubusercontent.com/81251379/212247805-63a36671-fb67-4be2-9831-a03706c32e6a.png)

Рисунок 1 - Пример представления информации в ПМ ИЭТР.</h1> 

При каждом новом дистрибутиве программного обеспечения ПМ ИЭТР требуется проводить тестирование нового функционала и соответсвенно уже сделанных ранее возможностей, чтобы убедиться, что ничего "не поехало" и ситема работает корректно.

На данном этапе сейчас это происходит в ручном режиме, опираясь на документ ПМИ - Программа и методика испытаний, в котором составляется на основе документа РД 50-34.698-90 и в нем указываются все проверки, которые определяют эффективность данного проектного решения.

__Главной задачей является переход от ручного к автоматизированному тестированию программного модуля ИЭТР.__

*В этом репозитории будет храниться код и отслеживаться изменения автотестов.*
