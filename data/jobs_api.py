import flask

from . import db_session
from .jobs import Jobs
from flask import jsonify, make_response

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('team_leader', 'collaborators', 'job', 'work_size', 'is_finished'))
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_jobs(jobs_id):
    db_sess = db_session.create_session()
    news = db_sess.get(Jobs, jobs_id)
    if not news:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'jobs': news.to_dict(only=(
                'team_leader', 'collaborators', 'job', 'work_size', 'is_finished'))
        }
    )