# DB

## User

|name|variable_name|type|remarks|
|-|-|-|-|
|ID|id|||
|ユーザー名|username|CharField|150字以下|
|パスワード|password|CharField|128字以下|
|所持金|money|IntegerField|default=0|
|ステータスポイント|st_point|IntegerField|default=0|
|体力|status_hp|IntegerField|default=1|
|腕力|status_arm|IntegerField|default=1|
|筋力|status_muscle|IntegerField|default=1，後で実装|
|幸運|status_luck|IntegerField|default=1|
|武器|weapon|ForeignKey||
|頭防具|equipment_head|ForeignKey|後で実装|
|胴体防具|equipment_body|ForeignKey|後で実装|
|腕防具|equipment_arm|ForeignKey|後で実装|
|足防具|equipment_leg|ForeignKey|後で実装|

## Weapon

|name|variable_name|type|remarks|
|-|-|-|-|
|ID|id|||
|名前|name|CharField|100字以下|
|攻撃力|atk|IntegerField|default=1|
|値段|price|IntegerField|default=0|
|必要腕力|required_arm|IntegerField|default=1|

## Equipment (後で実装)

|name|variable_name|type|remarks|
|-|-|-|-|
|ID|id|||
|防御力|def|IntegerField|default=1|
|値段|price|IntegerField|default=0|
|種類|type|CharField|choiceで設定|
|必要筋力|required_muscle|IntegerField|default=1|

type=['head','body','arm','leg']