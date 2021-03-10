# Do not modify these lines
__winc_id__ = '63ce21059cf34d3d8ffef497ede7e317'
__human_name__ = 'comments'

# Add your code after this line
""" comment1 
Voor deze comment-oefening hieronder heb ik de code overgenomen uit de calculate-oefening. """
print('Comment1 gaat het goed')
""" comment2 
multiline conmment1 - licht de aanpak van deze oefening toe
multiline comment2 - geeft de gevraagde uitleg bij de commentaarregels
single line comments 3 en 4 - geven toelichting op het blok code eronder 
end-of-line comments 5 en 6 - geven vertaling/toelichting van gedefinieerde variabelen """
print('Comment2 gaat ook goed')
# comment3 - hieronder worden verschillende groentenen hun prijzen gedefinieerd
broccoli = 2
leek = 2
potato = 3
brussel_sprout = 7
# comment4 - bovenstaande variabelen worden hieronder toegepast in verschillende prijsberekeningen
sum_one_each = (broccoli+leek+potato+brussel_sprout) 
avg_price = sum_one_each / 4                   # avg_price is gemiddelde prijs (comment5)
num_potatoes = 7
num_broccolis = 5
num_leeks = 2
num_brussel_sprouts = 10
sum_total = num_broccolis*2 + num_brussel_sprouts*7 + num_leeks*2 + num_potatoes*3
discount_percentage = 30               # discount_percentage = kortingspercentage (comment6)
discounted_sum_total = sum_total * (1 - discount_percentage/100)
print('De totale kortingsprijs van de som was: ', discounted_sum_total)
print('Maar eigenlijk ging het alleen om de comments.')
