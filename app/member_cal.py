
# 차례대호 수도권 여부, 모임명수, 백신 2차접종 2주경과인원, 모임 장소 종류(식당/카페 인지 확인)
def cal_moim(metropolitanAreaGet,moimNGet,vaccineNGet,moimLocationGet):
    metropolitanArea=metropolitanAreaGet
    moimN=moimNGet
    vaccineN=vaccineNGet
    moimLocation=moimLocationGet
      
    try:
        if(metropolitanArea=='수도권'):
            MaxLimitN=10 
            MinLimitN=4
            moimN=int(moimN)
            vaccineN=int(vaccineN)
            if(moimN<=MaxLimitN):   
                if(moimLocation=='식당/카페'):
                    if (moimN-vaccineN<=MinLimitN):                
                        return '모임 가능'
                    else:
                        return '모임 불가능'
                elif(moimLocation=='기타모임장소'):
                    return '모임 가능'
                else:
                    return '올바르게 입력해주세요'
            else:
                return '모임 불가능'
        elif(metropolitanArea=='비수도권'):
            MaxLimitN=12
            MinLimitN=4
            moimN=int(moimN)
            vaccineN=int(vaccineN)   
            if(moimN<=MaxLimitN):   
                if(moimLocation=='식당/카페'):
                    if (moimN-vaccineN<=MinLimitN):                
                        return '모임 가능'
                    else:
                        return '모임 불가능'
                elif(moimLocation=='기타모임장소'):
                    return '모임 가능'
                else:
                    return '올바르게 입력해주세요'
            else:
                return '모임 불가능'
        else:
            return '올바르게 입력해주세요'
    except:
        return '올바른 값을 입력해주세요'
    


