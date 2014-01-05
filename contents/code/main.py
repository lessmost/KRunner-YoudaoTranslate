from PyKDE4 import plasmascript
from PyKDE4.plasma import Plasma
from YDTranslate import YDTranslate


class YDTranslateRunner(plasmascript.Runner):
    def init(self):
        # called upon creation to let us run any initialization
        # tell the user how to use this runner
        self.addSyntax(
            Plasma.RunnerSyntax("yd :q:",
                                "Translate :q: using Youdao Translate"))
        self.translator = YDTranslate("456472771", "zqlu-github-io")

    def match(self, context):
        # called by krunner to let us add actions for the user
        if not context.isValid():
            return

        q = context.query()

        # look for our keyword 'yd'
        if not q.startsWith("yd "):
            return

        if q.length < 4:
            return

        # strip the keyword and leading space
        q = q[3:]
        q = q.trimmed()
        r = self.translator.translate(q)

        m = Plasma.QueryMatch(self.runner)
        m.setText(r)
        m.setType(Plasma.QueryMatch.ExactMatch)
        m.setData(q)
        context.addMatch(q, m)


def CreateRunner(parent):
    # called by krunner, must return an instance of the runner object
    return YDTranslateRunner(parent)
