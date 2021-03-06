import re
import typing
import DoodleServer.DoodleSql
from DoodleServer.DoodleOrm import *


class convert(object):
    eps: typing.Dict[int, Episodes]
    shots: typing.Dict[str, Shot]
    file_class: typing.Dict[str, fileClass]
    file_type: typing.Dict[str, fileType]
    ass_name: typing.Dict[str, assClass]

    def __init__(self):
        self.sql = DoodleServer.DoodleSql.commMysql("changanhuanjie")
        self.eps = {}
        self.shots = {}
        self.file_class = {}
        self.file_type = {}
        self.ass_name = {}

        self.tmp = []

    def convert(self):
        ass = ["character", "effects", "scane", "props"]
        sqlcom_2 = """SELECT `name`,localname FROM changanhuanjie.nametochinese"""
        with self.sql.engine.connect() as connect:
            assert isinstance(connect, sqlalchemy.engine.Connection)
            name_to_zhcn = connect.execute(sqlcom_2).fetchall()
        name_to_zhcn = {name[0]: name[1] for name in name_to_zhcn[:]}
        for __a in ass:
            self.file_type = {}
            self.ass_name = {}
            sqlcom = f"""SELECT `name`,`type`,`file`,`fileSuffixes`,`user`,`version`,`infor`,filepath,filestate,filetime FROM changanhuanjie.`{__a}`"""
            # 添加fileclass
            self.file_class[__a] = fileClass(file_class=__a)
            with self.sql.engine.connect() as connect:
                assert isinstance(connect, sqlalchemy.engine.Connection)
                ass_s = connect.execute(sqlcom).fetchall()

            for ass_name in {_ass_[0] for _ass_ in ass_s}:
                self.ass_name[ass_name] = assClass(file_name=ass_name)
                self.ass_name[ass_name].file_class = self.file_class[__a]
                try:
                    zn_name = name_to_zhcn[ass_name]
                except KeyError:
                    pass
                    # print("没有这个中文")
                else:
                    self.ass_name[ass_name].nameZNCH = ZNch(localname=zn_name)
                    name_to_zhcn.pop(ass_name)

            # for file_type in {_ass_[1] for _ass_ in ass_s}:

            for f_cls, f_type in {(_ass_[0], _ass_[1]) for _ass_ in ass_s}:
                self.file_type[f"{f_cls}_{f_type}"] = fileType(file_type=f_type)
                # 添加联系
                self.file_type[f"{f_cls}_{f_type}"].file_class = self.file_class[__a]
                self.file_type[f"{f_cls}_{f_type}"].ass_class = self.ass_name[f_cls]

            for _ass_s_ in ass_s:
                kwargs = {"file": _ass_s_[2], "fileSuffixes": _ass_s_[3], "user": _ass_s_[4], "version": _ass_s_[5],
                          "_file_path_": self.convertPathToIp(_ass_s_[7]), "infor": _ass_s_[6], "filetime": _ass_s_[9],
                          "filestate": _ass_s_[8]}
                ass_file = None
                if re.findall("sourceimages", _ass_s_[1]):
                    ass_file = assMapping(**kwargs)
                elif re.findall("scenes", _ass_s_[1]):
                    ass_file = assMayaScane(**kwargs)
                elif re.findall("_UE4", _ass_s_[1]):
                    ass_file = assUEScane(**kwargs)
                elif re.findall("rig", _ass_s_[1]):
                    ass_file = assMayaRigModel(**kwargs)
                elif re.findall("_low", _ass_s_[1]):
                    ass_file = assMayaLowModleModel(**kwargs)

                if ass_file:
                    # 添加联系
                    ass_file.file_class = self.file_class[__a]
                    ass_file.file_type = self.file_type[f"{_ass_s_[0]}_{_ass_s_[1]}"]
                    ass_file.ass_class = self.ass_name[_ass_s_[0]]

    def eps_shot(self):
        sqlcom = """SELECT episodes FROM changanhuanjie.mainshot"""
        with self.sql.engine.connect() as connect:
            assert isinstance(connect, sqlalchemy.engine.Connection)
            eps = connect.execute(sqlcom).fetchall()
        for ep in eps:
            self.eps[ep[0]] = (Episodes(episodes=ep[0]))
            self.shot(ep[0])

    def shot(self, ep):
        self.shots = {}
        self.file_class = {}
        self.file_type = {}
        sqlcom = f"""SELECT shot,shotab,department,`Type`,`file`,fileSuffixes,`user`,version,filepath,infor,filetime,filestate FROM `ep{ep:0>3d}`"""
        with self.sql.engine.connect() as connect:
            assert isinstance(connect, sqlalchemy.engine.Connection)
            shots = connect.execute(sqlcom).fetchall()

        for my_shot_0,my_shot_1,my_shot_2,my_shot_3 in [s[:4] for s in shots]:
            # 设置shot联系
            try:
                tmp = self.shots[f"{my_shot_0}_{my_shot_1}"]
            except KeyError:
                self.shots[f"{my_shot_0}_{my_shot_1}"] = Shot(shot_=my_shot_0, shotab=my_shot_1)
            self.eps[ep].addShot.append(self.shots[f"{my_shot_0}_{my_shot_1}"])

            # 设置fileclass联系
            try:
                tmp = self.file_class[f"{my_shot_0}_{my_shot_1}_{my_shot_2}"]
            except KeyError:
                self.file_class[f"{my_shot_0}_{my_shot_1}_{my_shot_2}"] = fileClass(file_class=my_shot_2)
            self.shots[f"{my_shot_0}_{my_shot_1}"].addfileClass.append(
                self.file_class[f"{my_shot_0}_{my_shot_1}_{my_shot_2}"])
            self.eps[ep].addFileClass.append(
                self.file_class[f"{my_shot_0}_{my_shot_1}_{my_shot_2}"])

            # 设置filetype联系
            try:
                tmp = self.file_type[f"{my_shot_0}_{my_shot_1}_{my_shot_2}_{my_shot_3}"]
            except KeyError:
                self.file_type[f"{my_shot_0}_{my_shot_1}_{my_shot_2}_{my_shot_3}"] = fileType(file_type=my_shot_3)
            self.file_class[f"{my_shot_0}_{my_shot_1}_{my_shot_2}"].addfileType.append(
                self.file_type[f"{my_shot_0}_{my_shot_1}_{my_shot_2}_{my_shot_3}"]
            )
            self.shots[f"{my_shot_0}_{my_shot_1}"].addfileType.append(
                self.file_type[f"{my_shot_0}_{my_shot_1}_{my_shot_2}_{my_shot_3}"]
            )
            self.eps[ep].addFileType.append(
                self.file_type[f"{my_shot_0}_{my_shot_1}_{my_shot_2}_{my_shot_3}"]
            )



        for shot_ in shots:
            kwargs = {"file": shot_[4], "fileSuffixes": shot_[5], "user": shot_[6], "version": shot_[7],
                      "_file_path_": self.convertPathToIp(shot_[8]), "infor": shot_[9], "filetime": shot_[10],
                      "filestate": shot_[11]}
            tmp_orm = None
            if shot_[2] == "VFX":
                tmp_orm = shotFlipBook(**kwargs)
            elif re.findall("[A,a]nm", shot_[2]):
                if re.findall("export", shot_[3]):
                    tmp_orm = shotMayaAnmExport(**kwargs)
                else:
                    tmp_orm = shotMayaAnmScane(**kwargs)
            elif shot_[2] == "Light":
                tmp_orm = shotMayaAnmExport(**kwargs)

            if tmp_orm:
                tmp_orm.episodes = self.eps[ep]
                tmp_orm.shot = self.shots[f"{shot_[0]}_{shot_[1]}"]

                tmp_orm.file_class = self.file_class[f"{shot_[0]}_{shot_[1]}_{shot_[2]}"]
                tmp_orm.file_type = self.file_type[f"{shot_[0]}_{shot_[1]}_{shot_[2]}_{shot_[3]}"]

            else:
                print(shot_[2], shot_[3])

    def subass(self):
        with self.sql.session() as session:
            assert isinstance(session, sqlalchemy.orm.session.Session)
            for key, name in self.file_class.items():
                session.add(name)

    def subeps(self):
        with self.sql.session() as session:
            assert isinstance(session, sqlalchemy.orm.session.Session)
            for key, ep in self.eps.items():
                session.add(ep)

    @staticmethod
    def convertPathToIp(path:str) -> pathlib.Path:
        """

        Args:
            path:

        Returns:

        """
        path = pathlib.Path(path)
        if path.drive:
            if path.drive.__len__() == 2:
                _path = path.as_posix()[2:]
            else:
                strlen = path.as_posix().split("/")[2].__len__() + 2
                _path = path.as_posix()[strlen:]
        else:
            _path = path.as_posix()
        # _path_ = pathlib.Path(_path)
        return _path


def run():
    test = convert()
    test.convert()
    test.subass()
    print(test)
    test.eps_shot()
    test.subeps()
    print(test)


if __name__ == '__main__':
    run()
