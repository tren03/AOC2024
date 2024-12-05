import re


# Takes a string and removes newline at the end of the string
def remove_newline(string: str) -> str:
    mod_string = string.removesuffix("\n")
    return mod_string


# Gets the data from the file
def get_data(filepath: str) -> list[str]:
    with open(filepath, "r") as file:
        return file.readlines()


# gets ("str","str") -> we convert to int, find product and return
def calc_prod(nos_tuple: tuple[str, str]) -> int:
    return int(nos_tuple[0]) * int(nos_tuple[1])


def calc_sum(nos_str: str | None) -> int:
    if not nos_str:
        return 0

    sum = 0

    result = re.findall(r"mul\((\d+)\,(\d+)\)", nos_str)
    for tup in result:
        sum += calc_prod(tup)

    return sum


def start_regex(string: str) -> str | None:
    start = re.search(r"(.*?)(?=don't\(\))", string)
    if start:
        # print(start.group())
        # if we have a do in this list, we would be counting it twice, so discard if do is present
        line_to_check_for_do = start.group()
        res_check_for_do = re.search(r"do()", line_to_check_for_do)
        if not res_check_for_do:
            return line_to_check_for_do
        else:
            print("do detected at the start")
            return None
    else:
        return None


def betweeen_regex(string: str) -> list[str]:
    between_do_dont = re.findall(r"do\(\)(.*?)don't\(\)", string)
    print(type(between_do_dont))
    return between_do_dont


def end_regex(string: str) -> str | None:
    end = re.search(r"do\(\)(.*?)$", string)
    if end:
        # if end containes dont, do not need to process this, since it would be included in the between part of regex
        line_to_check_for_dont = end.group()
        res_check_for_dont = re.search(r"don't()", line_to_check_for_dont)
        if not res_check_for_dont:
            return line_to_check_for_dont
        else:
            print("dont detected at the end")
            return None


if __name__ == "__main__":
    SAMPLE_INPUT_FILE = "../input/sample.txt"
    MAIN_INPUT_FILE = "../input/main.txt"
    final_sum = 0
    lines = get_data(MAIN_INPUT_FILE)
    # line_test = [
    #     "-:-]what()(+/mul(957,396)?mul(550,844)%+why())-? #}from()mul(488,628)%} ~**mul(770,931)$~mul(791,733)<{mul(985,350)<#why()don't()what()select()$what())]what()who()mul(327,185))<^^mul(542,68)#?who()<from()';^how()mul(619,952)/where(){(!);'@,mul(551,161)select()>when()do()from()mul(51,291)[where()!{]/}'@?mul(233,511)@what()]mul(311,967))&who()how()mul(839,578)^who()]}mul(266,735){mul(176,670)mul(154,710)*select()](':^,mul(531,801)# *why()why()mul(30,325)~,where();select()select()}-/when()mul(512,729)+where();[mul(720,339)[~*when()mul(722,867)!);{+mul(582,286)^:)what()@mul(604,485) (who()why()who()from()[mul(128,295)how()?!%~~<what()mul(156,267)'how(689,161):where()mul(206,221) mul(835,81);] %mul(562,798)^{%where()mul(38,166)#!what()mul(185,550)^! ?,+;}}mul(685,101)select()mul(316,869)>[~}{[&;mul(548,186))(%];mul(841,290)when()where()'?mul(646,803)mul(553,782)how()when()-mul(569,604)@ ++:/%why()]select()mul(257,598)#mul(897,819)how()what()from()how()]when()~/!}mul(856,271)+&why(){}why()>who()mul(373,408)-who()^&%>';,when()mul(54,88)what()!mul(663,711)$#(?;^from()mul(898,810)when()from()%@mul(776,102)why()mul(303,842)!/,%<^;mul(840,791){[@mul(909,714)don't()>who()why()from(545,686)%~mul(483,956)^'why()from()where()$>*:mul(931,649) mul(800,313)):mul(31,69)mul(549,670)$;mul(327,976)@who()^mul(627,907)/[@what(925,706) ;^who()!mul(629,813)when(){$&where(){#mul(504,147)?mul(222,429)#who()*/!select()<what()mul(310,934)])^/$]mul(917,911)-%how()?[;,mul(823,273)*[~select()/select()~%mul(703,815)what()where()?what():'?[who()mul(966,52)how()&-~(%[(^mul(913,694)mul(190,570),&<%'from()where()what(979,309):+mul(662,926)/<!when()'select(),/&*mul(655,410) how()}mul(386,934)where()[mul(159,595)@']from()when()#?@mul(356,559)&)>?$ mul(439,336)?from()*select()*}when()]who()mul(148,356)(who()+mul(271,905)mul(564,172)@?(~mul(628,470)#} mul(301,170)?@,^don't();&:^&how(605,264))(what()'mul(896,108),$mul(413,431):<>where();how()>!}when()do()!}/&:when()>mul(754,737)~:#:* mul(962,620)}mul(26,490)!~,mul(450,234){/]who() <;{mul(938,932)?--#%};}mul(140,314)(-}/,[mul(202,839)^why()-!},mul(459,716),mul(600,932)}when()]who()}who())&mul(752,142$mul(174,573)mul(231,182)from()mul(308,661)what()} mul(178,99)&^*[(mul(858,730)~}from()^mul(17,545)what()~{~*^what(90,714)how(),mul(63,969)-]mul(364,49);mul(130,598<:&why()select(879,794)mul(46,169)>&how()%mul(564,506)/what(255,868)mul(415,375)':@who()mul(525,772)<$mul(277,787)[~mul(314,321)'&@$^%mul(741,325)?(%#;*mul(459,703)why()~what()mul(250,38)what()<-$)when()%(don't()mul(296 ',mul(673,933)?#<@who()from()^?mul(831,912)?/*mul(407,853)mul(119what()why()>mul(816,762) how()<}~from()how()/@:mul(792,799)()@?%:$:mul(289,264)"
    # ]
    print(lines)
    for line in lines:
        line_to_process = remove_newline(line)

        #### NEW lOGIC ###
        start = start_regex(line_to_process)
        between = betweeen_regex(line_to_process)
        end = end_regex(line_to_process)

        final_sum += calc_sum(start)
        for s in between:
            print(f"EACH ELEMENT IN BETWEEN, TYPE {type(s)} :  {s}\n\n\n")
            final_sum += calc_sum(s)
        final_sum += calc_sum(end)

        print("-------------------------------------\n\n\n")
    print(f"final answer = {final_sum}")
