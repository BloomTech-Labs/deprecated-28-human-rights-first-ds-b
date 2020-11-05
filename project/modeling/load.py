import joblib
from modeling.build import TextMatcher

__all__ = ("TextMatcherModel",)
TextMatcherModel: TextMatcher = joblib.load('model.joblib')


if __name__ == '__main__':
    print()
    print(TextMatcherModel(
        "Disney tells Mickey Mouse to find a new job!"
    ))
    print(TextMatcherModel(
        "Police in riot gear are everywhere!"
    ))
    print(TextMatcherModel(
        "Police are pushing people to the ground!"
    ))
    print(TextMatcherModel(
        "Police are hitting people with batons and firing rubber bullets!"
    ))
    print(TextMatcherModel(
        "Police are spraying protesters with tear gas and pepper spray!"
    ))
    print(TextMatcherModel(
        "Police just killed that unarmed woman in cold blood!"
    ))
