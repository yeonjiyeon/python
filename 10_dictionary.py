# product = {'컵라면':800,'삼각김밥':1000,'소세지':1500}
# word = {'boy':'소년','girl':'소녀','family':'가족'}

# print(product)
# print(word)

#딕셔너리 추가-----------------------------------------
# product = {'컵라면':800,'삼각김밥':1000,'소세지':1500}
# product['오뎅'] = 2000
# product['닭다리'] = 3000
# product['아이스크림'] = 1000
# print(product)


#딕셔너리 삭제----------------------------------------
# product = {'컵라면':800,'삼각김밥':1000,'소세지':1500}
# del(product['컵라면'])
# del(product['소세지'])
# print(product)

#-------------------------------------------------
# product = {'컵라면':800,'삼각김밥':1000,'소세지':1500}
# print(product.get('삼각김밥'))
# print(product.keys())
# print(product.values())
# print(list(product.keys()))
# print(list(product.values()))

#in-----------------------------------------------------------
# product = {'컵라면':800,'삼각김밥':1000,'소세지':1500}
# item = input('상품을 입력하세요:')

# if(item in product):
#     print('편의점에 상품이 있습니다')
# else:
#     print('편의점에 존재하지 않는 상품입니다')

capital = {'네팔':'카트만두',
        '대한민국':'서울',
        '일본':'도쿄',
        '중국':'베이징',
        '이탈리아':'로마',
        '러시아':'모스크바',
        '독일':'베를린',
        '미국':'워싱턴',
        '프랑스':'파리',
        '영국':'런던'}

while(True):
    contry = input(str(list(capital.keys()))+'나라의 수도는 무엇일까요?')
    if contry in capital:
        print(contry,'의 수도는',capital.get(contry),'입니다')

    elif contry == "exit":
        break
    else:
        print('그런 나라가 없습니다')

