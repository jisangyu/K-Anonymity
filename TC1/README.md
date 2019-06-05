original.txt > 인철이형이 처음 준 데이터

auto_TermFreq.sh # 실행하면 자동으로 빈도수 추출, 


grep ",\"0\"" original.txt >original.neg

grep ",\"1\"" original.txt >original.pos


awk -F '\",\"' '{print $6}' original.pos >original.pos.condition
awk -F '\",\"' '{print $6}' original.neg >original.neg.condition


sort original.neg.condition >neg.condition.sort
sort original.pos.condition >pos.condition.sort


uniq -c neg.condition.sort >neg.condition.count
uniq -c pos.condition.sort >pos.condition.count

python run.py >temp


sort temp> temp.sort

