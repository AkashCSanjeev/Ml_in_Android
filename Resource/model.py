from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
import pickle,numpy as np,sklearn
import xgboost



list = []
class Model(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
            'level',
            type=float,
            required = True,
            help="level required for prediction"
    )
    

    def post(self):
        data = Model.parser.parse_args()
        RF = pickle.load(open('RF_regressor.pkl','rb'))
        # XG = pickle.load(open('XGregressor.pkl','rb'))
        x = np.array([[data['level']]])
        
        
        
        predictions = {
            'level':data['level'],
            'Random Forest': RF.predict(x)[0]
            # 'XG Boost':XG.predict(x)[0]
        }
        
        list.append(predictions)
        return {'salaries':list}
