from astrorecon.engine import summarize

def test_summarize():
    result = summarize('data/sample_catalog.json')
    assert result['assets'] == 3