<?php
// 随机生成10位数字ID，$autoID<=[数字种子，可取数据表的自增ID]
function auID($autoID)
{
    $autoID = $autoID;
    $autoCharacter = array("1","2","3","4","5","6","7","8","9","A","B","C","D","E");
    $len = 7-((int)log10($autoID) + 1);
    $i=1;
    $numberID = mt_rand(1, 2).mt_rand(1, 4);
    for($i;$i<=$len-1;$i++)
    {
        $numberID .= $autoCharacter[mt_rand(1, 13)];
    }

    return base_convert($numberID."E".$autoID, 16, 10);
}

$uuidArr = [];
$i=1;
if(intval($argv[1])<=0){
    var_dump('参数非法，必须为数字');
    return false;
}
$maxNum=intval($argv[1]);
while($i<=$maxNum){
    $uuidArr[] = auID($i);
    $i++;
}
$uuidArr = array_flip($uuidArr);
$uuidArrNum = count($uuidArr);
$repeatNum = $maxNum-$uuidArrNum;
var_dump($maxNum.'个测试ID里有重复ID有'.$repeatNum.'个');
return true;

